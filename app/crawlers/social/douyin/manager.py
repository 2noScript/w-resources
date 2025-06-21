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
# ===============================================================================


from app.crawlers.social.douyin.abogus import ABogus
from app.crawlers.social.douyin.xbogus import XBogus
from urllib.parse import  quote


class BogusManager:

    @classmethod
    def xb_str_2_endpoint(cls, endpoint: str, user_agent: str) -> str:
        try:
            final_endpoint = XBogus(user_agent).getXBogus(endpoint)
        except Exception as e:
            raise RuntimeError("Failed to generate X-Bogus: {0})".format(e))

        return final_endpoint[0]

    @classmethod
    def xb_model_2_endpoint(cls, base_endpoint: str, params: dict, user_agent: str) -> str:
        if not isinstance(params, dict):
            raise TypeError("The parameter must be of dictionary type.")

        param_str = "&".join([f"{k}={v}" for k, v in params.items()])

        try:
            xb_value = XBogus(user_agent).getXBogus(param_str)
        except Exception as e:
            raise RuntimeError("Failed to generate X-Bogus: {0})".format(e))

        separator = "&" if "?" in base_endpoint else "?"

        final_endpoint = f"{base_endpoint}{separator}{param_str}&X-Bogus={xb_value[1]}"

        return final_endpoint

    @classmethod
    def ab_model_2_endpoint(cls, params: dict, user_agent: str) -> str:
        if not isinstance(params, dict):
            raise TypeError("The parameter must be of dictionary type.")

        try:
            ab_value = ABogus().get_value(params, )
        except Exception as e:
            raise RuntimeError("生成A-Bogus失败: {0})".format(e))

        return quote(ab_value, safe='')

