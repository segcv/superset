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
import logging
from typing import List, Optional, TYPE_CHECKING

from sqlalchemy.exc import SQLAlchemyError

# from superset.charts.filters import ChartFilter
from superset.dao.base import BaseDAO
from superset.extensions import db
from superset.models.core import FavStar, FavStarClassName
from superset.models.ai_model_params import AIModelParams

if TYPE_CHECKING:
    from superset.connectors.base.models import BaseDatasource

logger = logging.getLogger(__name__)


class AIModelParamsDAO(BaseDAO):
    model_cls = AIModelParams
    # base_filter = ChartFilter

    # @staticmethod
    # def bulk_delete(models: Optional[List[Slice]], commit: bool = True) -> None:
    #     item_ids = [model.id for model in models] if models else []
    #     # bulk delete, first delete related data
    #     if models:
    #         for model in models:
    #             model.owners = []
    #             model.dashboards = []
    #             db.session.merge(model)
    #     # bulk delete itself
    #     try:
    #         db.session.query(Slice).filter(Slice.id.in_(item_ids)).delete(
    #             synchronize_session="fetch"
    #         )
    #         if commit:
    #             db.session.commit()
    #     except SQLAlchemyError as ex:
    #         if commit:
    #             db.session.rollback()
    #         raise ex

    @staticmethod
    def save(model: AIModelParams, commit: bool = True) -> None:
        print(model)
        db.session.add(model)
        if commit:
            db.session.commit()

    
    @staticmethod
    def list() -> List[AIModelParams]:
        from sqlalchemy.sql import text
        field_list = ['id','name']
        field_object_list = []
        for field in field_list:
            field_object_list.append(getattr(AIModelParams, field))
        rows = db.session.query(*field_object_list).order_by(text('update_time desc')).all()
        res = [ [r.id, r.name] for r in rows ]
        return res


    @staticmethod
    def get(id: int) -> List[AIModelParams]:
        from sqlalchemy.sql import text
        field_list = ['id','name', 'config', 'checkpoint']
        field_object_list = []
        for field in field_list:
            field_object_list.append(getattr(AIModelParams, field))
        row = db.session.query(*field_object_list).filter(text(f'id={id}')).order_by(text('update_time desc')).first()
        return row
    