# ==============================================================================
# Copyright (C) 2025 2noScript
#
# This project is licensed under the Apache License 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
#                       ,-,-
#                      / / |
#    ,-'             _/ / /
#   (-_          _,-' `Z_/
#    "#:      ,-'_,-.    \  _
#     #'    _(_-'_()\     \" |
#   ,--_,--'                 |
#  / ""                      L-'\
#  \,--^---v--v-._        /   \ |
#    \_________________,-'      |
#                     \          \
#                      \          \
#   Feed me Stars ⭐    \          \
# ==============================================================================


import traceback
from typing import Union
from fastapi import APIRouter, Form, status
from app.api.models.PolloRequest import PolloaiExplore
from app.utils.logging_utils import configure_logging
from app.crawlers.platforms.pollo.crawler import PolloCrawler
from app.api.models.APIBaseModel import ResponseModel, ErrorResponseModel


pollo_crawler = PolloCrawler()

router = APIRouter()

logger = configure_logging(name=__name__)


@router.get("/tags", response_model=ResponseModel)
async def get_tags() -> Union[ResponseModel, ErrorResponseModel]:
    return ResponseModel(data=pollo_crawler.fetch_tags())


@router.post(
    "/explore",
    response_description="Result information of exploring polloai",
)
async def get_explore(
    _PolloaiExplore: PolloaiExplore = Form(...),
) -> Union[ResponseModel, ErrorResponseModel]:
    try:
        data, metadata = await pollo_crawler.fetch_explore(
            tag=_PolloaiExplore.tag,
            sub_tag=_PolloaiExplore.sub_tag,
            limit=_PolloaiExplore.limit,
            cursor=_PolloaiExplore.cursor,
        )
        return ResponseModel(
            params=_PolloaiExplore.model_dump(),
            data=data,
            metadata=metadata,
        )
    except Exception as e:
        logger.error(f"Error: {e}")
        logger.error(traceback.format_exc())
        return ErrorResponseModel(
            code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
        )
