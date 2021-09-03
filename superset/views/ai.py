# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
import simplejson as json
from flask import g, redirect, request, Response
from flask_appbuilder import expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.security.decorators import has_access, has_access_api
from flask_babel import lazy_gettext as _

from superset import db, is_feature_enabled
from superset.constants import MODEL_VIEW_RW_METHOD_PERMISSION_MAP, RouteMethod
from superset.models.sql_lab import Query, SavedQuery, TableSchema, TabState
from superset.models.dashboard import Dashboard as DashboardModel
from superset.typing import FlaskResponse
from superset.utils import core as utils
from superset.views.dashboard.mixin import DashboardMixin


from superset.views.base import (
    BaseSupersetView,
    check_ownership,
    DeleteMixin,
    generate_download_headers,
    SupersetModelView,
)


class AIModelView(
    DashboardMixin, SupersetModelView, DeleteMixin
):  # pylint: disable=too-many-ancestors
    route_base = "/ai"
    datamodel = SQLAInterface(DashboardModel)
    # TODO disable api_read and api_delete (used by cypress)
    # once we move to ChartRestModelApi
    class_permission_name = "AI"
    method_permission_name = MODEL_VIEW_RW_METHOD_PERMISSION_MAP

    include_route_methods = RouteMethod.CRUD_SET | {
        RouteMethod.API_READ,
        RouteMethod.API_DELETE,
        "download_dashboards",
    }

    def pre_add(self, item: "AIModelView") -> None:
        utils.validate_json(item.params)

    def pre_update(self, item: "AIModelView") -> None:
        utils.validate_json(item.params)
        check_ownership(item)

    def pre_delete(self, item: "AIModelView") -> None:
        check_ownership(item)

    @expose("/train")
    def list(self) -> FlaskResponse:
        
        # return "<p>Hi, AI</p>"
        # return self.render_template("superset/ai/index.html")
        return super().render_app_template()