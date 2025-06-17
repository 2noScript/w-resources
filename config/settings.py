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


import os
from typing import Optional
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Settings:

    class FastAPISettings:
        # Project name
        title: str = "Free-resources-from-many-sources"
        # Project description
        description: str = "All free"
        # Project version
        version: str = "0.0.1"
        # Swagger docs URL
        docs_url: str = "/docs"
        # Whether to enable debug mode
        debug: bool = False
        # Whether to automatically reload the project when changes to the project code are detected
        reload_on_file_change: bool = os.getenv("RELOAD_ON_FILE_CHANGE", False)
        # FastAPI service IP
        ip: str = "0.0.0.0"
        # FastAPI service port
        port: int = 80

    class LogSettings:
        # Log level
        """
        CRITICAL = 50
        FATAL = CRITICAL
        ERROR = 40
        WARNING = 30
        WARN = WARNING
        INFO = 20
        DEBUG = 10
        NOTSET = 0
        """
        level: int = 10
        #  Log file directory
        log_dir: str = "./log_files"
        #  Log file prefix
        log_file_prefix: str = "app"
        #  Log file encoding
        encoding: str = "utf-8"
        #  Log file backup count
        backup_count: int = 7

    class PolloSettings:
        # Polloai Web Cookie
        cookie: str = os.getenv("POLLO_COOKIE", "")
        # Polloai Proxy
        proxy: str = os.getenv("POLLO_PROXY", None)

        version: str = "0.0.1"



