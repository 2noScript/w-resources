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


from app.api.models.DataBaseModel import Data, DataType, MediaType, Video
from app.crawlers.platforms.pollo.endpoints import PolloEndpoints
from config.settings import Settings
from tenacity import retry, stop_after_attempt
from app.utils.serializers_utils import class_to_dict
from app.crawlers.platforms.pollo.tags import PolloTags
from typing import Optional
from curl_cffi import AsyncSession
from typing import Optional, List
import json


class PolloCrawler:

    def fetch_tags(self):
        return {
            "tags": PolloTags,
            "count": len(PolloTags),
        }

    def extract_data(self, raw_data) -> List[Data]:
        data: List[Data] = []
        for item in raw_data:
            if item["mediaType"] == "video":
                video = Video(
                    title=item["title"],
                    thumbnail=item["cover"],
                    video_url=item["videoUrl"],
                    video_url_nwm=item["videoUrlNoWatermark"],
                    duration_ms=item["durationMs"],
                    keywork=item["tags"],
                    star=item["starNum"],
                    share=item["shareNum"],
                )
                data.append(
                    Data(
                        id=item["videoId"],
                        prompt=item["generateRecord"]["prompt"],
                        data_type=DataType.AI_GENERATOR,
                        media_type=[MediaType.VIDEO],
                        video=video,
                    )
                )

        return data

    @retry(
        stop=stop_after_attempt(3),
        retry_error_callback=lambda retry_state: retry_state.outcome.result(),
    )
    async def fetch_explore(
        self, tag: str, sub_tag: str, limit: int = 20, cursor: Optional[str] = None
    ):
        params = {
            "batch": 1,
            "input": json.dumps(
                {
                    "0": {
                        "json": {
                            "limit": limit,
                            "score": "desc",
                            "type": tag,
                            "tag": sub_tag,
                            "cursor": cursor,
                        },
                        "meta": {"values": {"cursor": ["undefined"]}},
                    }
                }
            ),
        }
        async with AsyncSession(impersonate="chrome") as session:
            response = await session.get(
                url=PolloEndpoints.EXPLORER_ROOT, params=params
            )
        res_json = response.json()
        data = self.extract_data(res_json[0]["result"]["data"]["json"]["data"])
        metadata = {
            "current_cursor": cursor,
            "next_cursor": res_json[0]["result"]["data"]["json"]["nextCursor"],
        }
        return data, metadata
