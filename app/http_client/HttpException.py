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

class APIError(Exception):
    """
    Base API exception class for all API-related errors.
    Other API exception classes inherit from this class.
    """

    def __init__(self, message: str = "An HTTP Client error occurred.", status_code: int = None):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        """
        Return formatted error message.

        :return: Error message string
        """
        return f"{self.message}" + (f" Status Code: {self.status_code}." if self.status_code else "")


class APIConnectionError(APIError):
    """Raised when there is a connection issue with the API."""

    def __init__(self, message: str = "Error occurred while connecting to the target server.", status_code: int = None):
        super().__init__(message, status_code)


class APIUnavailableError(APIError):
    """Raised when the API service is unavailable, e.g., maintenance or timeout."""

    def __init__(self, message: str = "The target server is currently unavailable.", status_code: int = 503):
        super().__init__(message, status_code)


class APINotFoundError(APIError):
    """Raised when the API endpoint does not exist."""

    def __init__(self, message: str = "The requested target server endpoint was not found.", status_code: int = 404):
        super().__init__(message, status_code)


class APIResponseError(APIError):
    """Raised when the API response is not as expected."""

    def __init__(self, message: str = "Unexpected target server response.", status_code: int = None):
        super().__init__(message, status_code)


class APIRateLimitError(APIError):
    """Raised when the API rate limit has been reached."""

    def __init__(self, message: str = "Target server rate limit exceeded.", status_code: int = 429):
        super().__init__(message, status_code)


class APITimeoutError(APIError):
    """Raised when the API request times out."""

    def __init__(self, message: str = "The target server request timed out.", status_code: int = 408):
        super().__init__(message, status_code)


class APIUnauthorizedError(APIError):
    """Raised when the API request is unauthorized."""

    def __init__(self, message: str = "Unauthorized target server request.", status_code: int = 401):
        super().__init__(message, status_code)


class APIRetryExhaustedError(APIError):
    """Raised when the API retry attempts are exhausted."""

    def __init__(self, message: str = "Target server retry limit exhausted.", status_code: int = None):
        super().__init__(message, status_code)


class APIFileDownloadError(APIError):
    """Raised when there is an issue downloading a file."""

    def __init__(self, message: str = "Failed to download the file.", status_code: int = None):
        super().__init__(message, status_code)
