import json
import logging
from typing import Any, Dict, Optional, Type, TYPE_CHECKING
from urllib import parse

import sqlalchemy as sqla
from flask_appbuilder import Model
from flask_appbuilder.models.decorators import renders
from markupsafe import escape, Markup
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table, Text, BLOB
from sqlalchemy.engine.base import Connection
from sqlalchemy.orm import relationship
from sqlalchemy.orm.mapper import Mapper

from superset import ConnectorRegistry, db, is_feature_enabled, security_manager
from superset.legacy import update_time_range
from superset.models.helpers import AuditMixinNullable, ImportExportMixin
from superset.models.tags import ChartUpdater
from superset.tasks.thumbnails import cache_chart_thumbnail
from superset.utils import core as utils
from superset.utils.hashing import md5_sha_from_str
from superset.utils.memoized import memoized
from superset.utils.urls import get_url_path
from superset.viz import BaseViz, viz_types


class AIModelParams( 
    Model, AuditMixinNullable, ImportExportMixin
):
    """AI Model Paramters store checkpoint of model"""
    __tablename__ = "ai_model_params"

    list_columns = ['id', 'name', 'slice_id', 'checkpoint', 'create_time', 'update_time', 'is_delete']

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    slice_id = Column(Integer)
    checkpoint = Column(BLOB)
    create_time = Column(String(50))
    update_time = Column(String(50))
    is_delete = Column(Integer, default=0)