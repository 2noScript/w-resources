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


import logging
import os
import sys
from concurrent_log_handler import ConcurrentRotatingFileHandler
from config.settings import Settings
from typing import Optional


def configure_logging(
    name: Optional[str] = None,
    log_level: int = Settings.LogSettings.level,
    log_dir: Optional[str] = Settings.LogSettings.log_dir,
    log_file_prefix: Optional[str] = Settings.LogSettings.log_file_prefix,
    backup_count: int = Settings.LogSettings.backup_count,
    encoding: str = Settings.LogSettings.encoding
) -> logging.Logger:
    """
    A logger that supports log rotation and console output, using the ConcurrentRotatingFileHandler handler.

    :param name: The name of the logger, default is None, using the root logger.
    :param log_level: The log level, default is logging.DEBUG.
    :param log_dir: The log file directory, default is './log_files'.
    :param log_file_prefix: The log file prefix, default is 'app'.
    :param backup_count: The number of backup files to keep, default is 7.
    :param encoding: The log file encoding, default is 'utf-8'.
    :return: The configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent duplicate handlers
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Create log directory
        if log_dir:
            log_dir = os.path.abspath(log_dir)
            os.makedirs(log_dir, exist_ok=True)

        # Configure concurrent log rotation handler
        if log_file_prefix:
            log_file_name = f"{log_file_prefix}.log"
            log_file_path = os.path.join(log_dir, log_file_name)
            rotating_file_handler = ConcurrentRotatingFileHandler(
                filename=log_file_path,
                # Set max file size to 10 MB
                maxBytes=10*1024*1024,
                backupCount=backup_count,
                encoding=encoding,
            )
            rotating_file_handler.setFormatter(formatter)
            logger.addHandler(rotating_file_handler)

        # Configure console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
