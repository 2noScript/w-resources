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




from typing import Union
from fastapi import APIRouter, Form, status
from app.api.models.APIBaseModel import ResponseModel, ErrorResponseModel
from app.utils.logging_utils import configure_logging
from app.crawlers.generative.hailuoai.crawler import HailuoaiCrawler
from config.settings import Settings
from app.api.models.APIBaseModel import RequestModel



crawler = HailuoaiCrawler()

router = APIRouter()

logger = configure_logging(name=__name__)



@router.get("/tags", response_model=ResponseModel)
async def get_tags() -> Union[ResponseModel, ErrorResponseModel]:
    return ResponseModel(data=crawler.fetch_tags(),version=Settings.HailuoaiSettings.version)

@router.post(
    "/explore",
    response_description="Result information of exploring polloai",
)
async def get_explore(
    request: RequestModel = Form(...),
) -> Union[ResponseModel, ErrorResponseModel]:
    try:
        data, metadata = await crawler.fetch_explore(
            tag=request.tag,
            sub_tag=request.sub_tag,
            limit=request.limit,
            cursor=request.cursor,
        )
        return ResponseModel(
            params=request.model_dump(),
            data=data,
            metadata=metadata,
            version=Settings.HailuoaiSettings.version
        )
    except Exception as e:
        logger.error(f"Error: {e}")
        return ErrorResponseModel(
            code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(e),
            version=Settings.HailuoaiSettings.version
        )
