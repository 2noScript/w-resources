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


from app.crawlers.platforms.promeai.tags import PromeaiTags


class PromeaiCrawler:

    def fetch_tags(self):
        return {
            "tags": PromeaiTags,
            "count": len(PromeaiTags),
        }
    
    async def fetch_explore(self, tag: str, sub_tag: str, limit: int = 20, cursor: str = None):
        return {
            "tag": tag,
            "sub_tag": sub_tag,
            "limit": limit,
            "cursor": cursor,
        }