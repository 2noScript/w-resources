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

from fastapi import APIRouter
from app.api.routers import (
    health_check,
    pollo_resource,
    promeai_resource,
    seaart_resource,
    vidu_resource,
    artlist_resource,
    hailuoai_resource,
    klingai_resource,
)


router = APIRouter()


# Health Check routers
router.include_router(health_check.router, prefix="/health", tags=["Health-Check"])

# Polloai Resource
router.include_router(pollo_resource.router, prefix="/polloai", tags=["Pollo"])

# Promeai Resource
router.include_router(promeai_resource.router, prefix="/promeai", tags=["Promeai"])

# Seaart Resource
router.include_router(seaart_resource.router, prefix="/seaart", tags=["Seaart"])

# Vidu Resource
router.include_router(vidu_resource.router, prefix="/vidu", tags=["Vidu"])

# Artlist Resource
router.include_router(artlist_resource.router, prefix="/artlist", tags=["Artlist"])

# Hailuoai Resource
router.include_router(hailuoai_resource.router, prefix="/hailuoai", tags=["Hailuoai"])

# Klingai Resource
router.include_router(klingai_resource.router, prefix="/klingai", tags=["Klingai"])
