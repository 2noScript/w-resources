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

from app.utils.logging_utils import configure_logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.router import router as api_router
from app.utils.logging_utils import configure_logging
from config.settings import Settings


# Configure the logger
logger = configure_logging(name=__name__)

# API Tags
tags_metadata = [
    {"name": "Health-Check", "description": "**Server Health Check**"},
    {"name": "Pollo", "description": "Resources created by artificial intelligence"},
    {"name": "Promeai", "description": "Resources created by artificial intelligence"},
    {"name": "Seaart", "description": "Resources created by artificial intelligence"},
]


@asynccontextmanager
async def lifespan(application: FastAPI):
    pass


app = FastAPI(
    title=Settings.FastAPISettings.title,
    description=Settings.FastAPISettings.description,
    version=Settings.FastAPISettings.version,
    openapi_tags=tags_metadata,
    docs_url=Settings.FastAPISettings.docs_url,
    debug=Settings.FastAPISettings.debug,
    # lifespan=lifespan,
)

# API Router
app.include_router(api_router, prefix="/api")
