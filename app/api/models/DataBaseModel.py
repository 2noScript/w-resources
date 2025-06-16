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


from pydantic import BaseModel
from typing import Optional, List, Union
from enum import Enum


class DataType(Enum):
    AI_GENERATOR = "ai_generator"
    AI_AUDIO = "ai_audio"


class MediaType(Enum):
    VIDEO = "video"
    AUDIO = "audio"
    IMAGE = "image"


class Video(BaseModel):
    title: Optional[str] = None
    thumbnail: Optional[str] = None
    video_url: Optional[str] = None
    video_url_nwm: Optional[str] = None
    duration_ms: int = 0
    keywork: List[str] = []
    star: Optional[int] = None
    share: Optional[int] = None


class Audio(BaseModel):
    title: str = ""
    audio_url: Optional[str] = None
    star: Optional[int] = None
    duration_ms: int = 0


class Image(BaseModel):
    title: str = ""
    image_url: str


class ExploreData(BaseModel):
    id: Union[str, int]

    data_type: DataType
    media_type: List[MediaType]

    prompt: Optional[str] = None
    model: Optional[str] = None
    video: Optional[Video] = None
    image: Optional[Image] = None


class AudioData(BaseModel):
    id: Union[str, int]
    data_type: DataType
    prompt: Optional[str] = None
    model: Optional[str] = None
    audio: Audio
