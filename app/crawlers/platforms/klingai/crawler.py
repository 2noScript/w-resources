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


from app.crawlers.BaseCrawler import BaseCrawler
from app.crawlers.platforms.klingai.endpoints import KlingaiEndpoints
from app.crawlers.platforms.klingai.tags import KlingaiTags
from app.api.models.DataBaseModel import ExploreData, DataType, MediaType, Video, Image
from typing import List
from curl_cffi import AsyncSession
from config.settings import Settings
import json


class KlingaiCrawler(BaseCrawler):

    def find_argument_value(self, arguments, target_name):
        for arg in arguments:
            if arg["name"] == target_name:
                return arg["value"]
        return None

    def extract_data(self, raw_data) -> List[ExploreData]:
        data: List[ExploreData] = []

        for item in raw_data:
            explore_data = ExploreData(
                id=item.get("taskId"),
                data_type=DataType.AI_GENERATOR,
                media_type=MediaType.VIDEO,
                model=self.find_argument_value(item["taskInfo"]["arguments"], "biz"),
                prompt=self.find_argument_value(
                    item["taskInfo"]["arguments"], "prompt"
                ),
            )
            print(
                self.find_argument_value(item["taskInfo"]["arguments"], "aspect_ratio")
            )
            if item["contentType"] == "video":
                explore_data.media_type = MediaType.VIDEO
                explore_data.video = Video(
                    title=item.get("title"),
                    thumbnail=item["cover"]["resource"],
                    video_url=item["resource"]["resource"],
                    duration_ms=item["resource"]["duration"],
                    video_ratio=f"{item["resource"]["width"]}:{item["resource"]["height"]}",
                    width=item["resource"]["width"],
                    height=item["resource"]["height"],
                )
            elif item["contentType"] == "image":
                explore_data.media_type = MediaType.IMAGE
                explore_data.image = Image(
                    title=item.get("title"),
                    image_url=item["resource"]["resource"],
                    # image_url_nwm=item["resource"]["resource"],
                    width=item["resource"]["width"],
                    height=item["resource"]["height"],
                )
            data.append(explore_data)

        return data

    def fetch_tags(self):
        return KlingaiTags

    async def fetch_explore(self, tag, sub_tag, limit, cursor):
        params = {
            "pageNum": int(cursor) if cursor else 1,
            "pageSize": limit,
            "sortType": sub_tag,
            "contentType": tag,
            "isCommunity": True,
            "match": "",
            "entrance": "community",
        }

        async with AsyncSession(
            impersonate="chrome", proxy=Settings.KlingaiSettings.proxy
        ) as session:
            response = await session.get(KlingaiEndpoints.EXPLORER_ROOT, params=params)

            if response.status_code != 200:
                raise Exception(
                    {
                        "crawl_status": response.status_code,
                        "crawl_message": response.text,
                    }
                )
        res_json = response.json()
        data = self.extract_data(res_json["data"])
        metadata = {
            "current_cursor": cursor,
            "next_cursor": res_json["pcursor"],
        }

        return data, metadata
