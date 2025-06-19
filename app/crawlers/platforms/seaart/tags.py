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


#  Graphic: picture
#  Article: article
#  Video:video

# order_by|timeType|sub_channel

SeaArtTags = [
    {
        "name": "Inspiration",
        "value": "post",
        "subtags": [
            {"name": "New", "value": "new"},
            {"name": "New Graphic", "value": "new|picture"},
            {"name": "New Article", "value": "new|article"},
            {"name": "New Video", "value": "new|video"},
            {"name": "Hot", "value": "hot"},
            {"name": "Hot Graphic", "value": "hot|picture"},
            {"name": "Hot Article", "value": "hot|article"},
            {"name": "Hot Video", "value": "hot|video"},
        ],
    },
    {
        "name": "AI Apps",
        "value": "app",
        "subtags": [
            {"name": "New", "value": "new"},
            {"name": "New Video Generation", "value": "new|video"},
            {"name": "New Image Generation", "value": "new|image"},
            {"name": "Hot", "value": "hot"},
            {"name": "Hot Graphic", "value": "hot|picture"},
            {"name": "Hot Article", "value": "hot|article"},
            {"name": "Hot Video", "value": "hot|video"},
        ],
    },
    {
        "name": "AI Characters",
        "value": "character",
        "subtags": [
            {"name": "New", "value": "new"},
            {"name": "Hot", "value": "hot"},
        ],
    },
    # {"name": "AI Audio", "value": "timbre"},
    {
        "name": "Models",
        "value": "model",
        "subtags": [{"name": "New", "value": "new"}, {"name": "Hot", "value": "hot"}],
    },
    # {"name": "AI Video", "value": "artwork"},
]
