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
from app.crawlers.BaseGenerativeCrawler import BaseGenerativeCrawler
from app.crawlers.generative.seaart.tags import SeaArtTags
from app.crawlers.generative.seaart.endpoints import SeaartEndpoints
from curl_cffi import AsyncSession
from config.settings import Settings
from typing import List


class SeaartCrawler(BaseGenerativeCrawler):

    def __get_url_explore(self, tag):
        if tag == "post":
            return SeaartEndpoints.EXPLORER_INSPIRATION
        elif tag == "app":
            return SeaartEndpoints.EXPLORER_AI_APP
        elif tag == "character":
            return SeaartEndpoints.EXPLORER_CHARACTERS
        elif tag == "model":
            return SeaartEndpoints.EXPLORER_MODEL
        return None

    def extract_data(self, raw_data) -> List[ExploreData]:
        data: List[ExploreData] = []

        for item in raw_data:
            explore_data = ExploreData(
                id=item["id"],
                data_type=DataType.AI_GENERATOR,
            )
            if item["content_type"] == "0":
                explore_data.media_type=MediaType.VIDEO
                explore_data.video = Video(
                    title=item.get("title"),
                    thumbnail=item["cover"]["url"],
                    video_url_nwm=item["stream"]["url3"],
                    width=item["cover"]["width"],
                    height=item["cover"]["height"],
                    video_ratio=f"{item['cover']['width']}:{item['cover']['height']}",
                )
            elif item["content_type"] == "1":
                explore_data.media_type=MediaType.IMAGE
                explore_data.image = Image(
                    title=item.get("title"),
                    image_url_nwm=item["cover"]["url"],
                    width=item["cover"]["width"],
                    height=item["cover"]["height"],
                    image_ratio=f"{item['cover']['width']}:{item['cover']['height']}",
                )

            data.append(explore_data)

        return data

    def fetch_tags(self):
        return SeaArtTags

    async def fetch_explore(self, tag: str, sub_tag: str, limit: int, cursor: str):
        params = {
            "offset": "",
            "page": int(cursor) if cursor else 1,
            "page_size": limit,
            "timeType": "All",
            "order_by": "hot",
            "order_by_time": "hot",
            "sub_channel": [],
            "tones": [],
            "languages": [],
            "genders": [],
            "ages": [],
            "model_types": [],
            "base_models": [],
            "run_available": 0,
            "nodes_type": [],
            "source_types": [],
            "tag_ids": [],
            "character_type": 0,
            "output_types": [],
        }

        url = self.__get_url_explore(tag)
        sub_tag_arr = sub_tag.split("|")
        if len(sub_tag_arr) == 2:
            if sub_tag_arr[0] == "new":
                params["order_by"] = sub_tag_arr[0]
                params["order_by_time"] = ""
            params["sub_channel"] = [sub_tag_arr[1]]

        async with AsyncSession(
            impersonate="chrome", proxy=Settings.SeaartSettings.proxy
        ) as session:
            response = await session.post(url, json=params)
        if response.status_code != 200:
            raise Exception(
                {
                    "crawl_status": response.status_code,
                    "crawl_message": response.text,
                }
            )
        res_json = response.json()
        data = self.extract_data(res_json["data"]["items"])
        metadata = {
            "current_cursor": cursor,
            "next_cursor": params["page"] + 1,
        }

        return data, metadata
