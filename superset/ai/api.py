import json
import logging
from datetime import datetime
from io import BytesIO
from typing import Any, Dict, Optional
from zipfile import ZipFile

import simplejson
from flask import g, make_response, redirect, request, Response, send_file, url_for
from flask_appbuilder.api import expose, protect, rison, safe
from flask_appbuilder.hooks import before_request
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import gettext as _, ngettext
from marshmallow import ValidationError
from werkzeug.wrappers import Response as WerkzeugResponse
from werkzeug.wsgi import FileWrapper

from superset import is_feature_enabled, thumbnail_cache
from superset.charts.commands.bulk_delete import BulkDeleteChartCommand
from superset.charts.commands.create import CreateChartCommand
from superset.charts.commands.data import ChartDataCommand
from superset.charts.commands.delete import DeleteChartCommand
from superset.charts.commands.exceptions import (
    ChartBulkDeleteFailedError,
    ChartCreateFailedError,
    ChartDataCacheLoadError,
    ChartDataQueryFailedError,
    ChartDeleteFailedError,
    ChartForbiddenError,
    ChartInvalidError,
    ChartNotFoundError,
    ChartUpdateFailedError,
)
from superset.charts.commands.export import ExportChartsCommand
from superset.charts.commands.importers.dispatcher import ImportChartsCommand
from superset.charts.commands.update import UpdateChartCommand
from superset.charts.dao import ChartDAO
from superset.charts.filters import ChartAllTextFilter, ChartFavoriteFilter, ChartFilter
from superset.charts.post_processing import apply_post_process
from superset.charts.schemas import (
    CHART_SCHEMAS,
    ChartPostSchema,
    ChartPutSchema,
    get_delete_ids_schema,
    get_export_ids_schema,
    get_fav_star_ids_schema,
    openapi_spec_methods_override,
    screenshot_query_schema,
    thumbnail_query_schema,
)
from superset.commands.importers.exceptions import NoValidFilesFoundError
from superset.commands.importers.v1.utils import get_contents_from_bundle
from superset.constants import MODEL_API_RW_METHOD_PERMISSION_MAP, RouteMethod
from superset.exceptions import QueryObjectValidationError
from superset.extensions import event_logger, security_manager
from superset.models.slice import Slice
from superset.models.ai_model_params import AIModelParams
from superset.tasks.thumbnails import cache_chart_thumbnail
from superset.utils.async_query_manager import AsyncQueryTokenException
from superset.utils.core import (
    ChartDataResultFormat,
    ChartDataResultType,
    json_int_dttm_ser,
)
from superset.utils.screenshots import ChartScreenshot
from superset.utils.urls import get_url_path
from superset.views.base_api import (
    BaseSupersetModelRestApi,
    RelatedFieldFilter,
    statsd_metrics,
)
from superset.views.core import CsvResponse, generate_download_headers
from superset.views.filters import FilterRelatedOwners

logger = logging.getLogger(__name__)

from superset.ai.ai_model_param_dao import AIModelParamsDAO

class AIRestApi(BaseSupersetModelRestApi):
    datamodel = SQLAInterface(AIModelParams)

    resource_name = "ai"
    allow_browser_login = True

    @expose("/list")
    def list(self):
        res = AIModelParamsDAO.list()
        return json.dumps(res)
