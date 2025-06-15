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


from datetime import datetime
from typing import Any, Optional, Dict
from pydantic import BaseModel, Field
from fastapi import Form



class RequestModel(BaseModel):
    tag: str = Form(
        default="",
        description="The tag of the resource",
        example="anime",
    )
    sub_tag: str = Form(
        default="",
        description="The sub tag of the resource",
        example="anime",
    )
    limit: int = Form(
        default=20,
        description="The limit of the resource",
        example=20,
    )


# Create a common response model
class ResponseModel(BaseModel):
    code: int = Field(default=200, description="HTTP status code")
    router: str = Field(
        default="",
        description="The endpoint that generated this response ",
    )
    params: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="The parameters used in the request ",
    )
    data: Optional[Any] = Field(default=None, description="The response data")
    
    metadata:Optional[dict] = Field(default_factory=dict,description="The continuation metadata")

    

    class Config:
        schema_extra = {
            "example": {
                "code": 200,
                "router": "/example/endpoint",
                "params": {"query": "example"},
                "data": {"key": "value"},
            }
        }


#  Define an error response model
class ErrorResponseModel(BaseModel):
    code: int = Field(default=400, description="HTTP status code")
    message: str = Field(
        default="An error occurred. ",
        description="Error message ",
    )
    time: str = Field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        description="The time the error occurred ",
    )
    router: str = Field(
        default="",
        description="The endpoint that generated this response",
    )
    params: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="The parameters used in the request",
    )

    class Config:
        schema_extra = {
            "example": {
                "code": 400,
                "message": "Invalid request parameters.",
                "time": "2025-10-27 14:30:00",
                "router": "/example/endpoint",
                "params": {"param1": "invalid"},
            }
        }


