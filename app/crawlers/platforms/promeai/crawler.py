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

from app.api.models.DataBaseModel import ExploreData, DataType, MediaType, Video, Image
from app.crawlers.BaseCrawler import BaseCrawler
from app.crawlers.platforms.promeai.tags import PromeaiTags
from curl_cffi import AsyncSession
from config.settings import Settings
from app.crawlers.platforms.promeai.endpoints import PromeaiEndpoints
from typing import Optional, List
import json


class PromeaiCrawler(BaseCrawler):

    def fetch_tags(self):
        return {
            "tags": PromeaiTags,
            "count": len(PromeaiTags),
        }

    def extract_data(self, raw_data) -> List[ExploreData]:
        data: List[ExploreData] = []
        for item in raw_data:
            explore_data = ExploreData(
                id=item["id"],
                data_type=DataType.AI_GENERATOR,
                prompt=item.get("prompt"),
                model=item.get("modelName"),
            )

            if item["isVideo"]:
                explore_data.media_type=MediaType.VIDEO
                explore_data.video = Video(
                    title=item["title"],
                    thumbnail=item["imageUrl"],
                    video_url=item["result"],
                    keywork=json.loads(item.get("tag")) if item.get("tag") else [],
                    video_ratio=item.get("styleInfoJson", {}).get("scale"),
                    width=item.get("width"),
                    height=item.get("height"),
                )
            else:
                explore_data.media_type=MediaType.IMAGE
                explore_data.image = Image(
                    title=item["title"],
                    image_url=None,
                    image_url_nwm=item["result"],
                    keywork=json.loads(item.get("tag")) if item.get("tag") else [],
                    width=item.get("width"),
                    height=item.get("height"),
                )
                
            data.append(explore_data)
        return data


    async def fetch_explore(
        self, tag: str, sub_tag: str, limit: int = 20, cursor: str = None
    ):
        params = {
            "pageNum": 1,
            "pageSize": limit,
            "searchType": 5,
            "source": tag,
            "styleId": "",
            "trendSearch": True,
            "tag": sub_tag,
        }

        if cursor:
            page, lastUpdatedAt = cursor.split(":")
            params["lastUpdatedAt"] = lastUpdatedAt
            params["pageNum"] = int(page)

        async with AsyncSession(
            impersonate="chrome", proxy=Settings.PromeaiSettings.proxy
        ) as session:
            response = await session.post(PromeaiEndpoints.EXPLORER_ROOT, json=params)
        if response.status_code != 200:
            raise Exception(
                {"crawl_status": response.status_code, "crawl_message": response.text}
            )
        res_json = response.json()
        data = []
        metadata = {
            "current_cursor": cursor,
            "next_cursor": None,
        }
        if res_json["data"]["content"]:
            data = self.extract_data(res_json["data"]["content"])
            metadata["next_cursor"] = (
                f"{params["pageNum"] + 1}:{res_json["data"]["content"][-1]["updatedAt"]}"
            )

        return data, metadata
