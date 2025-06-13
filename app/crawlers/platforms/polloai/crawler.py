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


import httpx
from app.crawlers.platforms.polloai.endpoints import PolloaiEndpoints
from config.settings import Settings


class PolloAiCrawler:

    async def get_headers(self):
        Cookie = Settings.PolloaiSettings.cookie
        if not Cookie:
            raise ValueError("Please configure the Polloai Web Cookie")

        kwargs = {
            "headers": {
                "Cookie": Cookie,
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                "User-Agent": "Googlebot-Image/1.0",
                "Referer": "https://pollo.ai/ai-effects/AI%20Twerk%20Video%20Generator",
            },
            "proxies": {
                "http://": Settings.DouyinAPISettings.proxy,
                "https://": Settings.DouyinAPISettings.proxy,
            },
        }
        return kwargs
