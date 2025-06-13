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


import traceback
from typing import Union
from fastapi import Request, APIRouter, HTTPException, Form, status
from app.utils.logging_utils import configure_logging
from app.crawlers.platforms.polloai.crawler import PolloAiCrawler


polloai_crawler = PolloAiCrawler()



router = APIRouter()

logger = configure_logging(name=__name__)

@router.post("/explore")
async def get_explore():
    return {}

@router.post("/audio")
async def get_audio_list():
    return {}



