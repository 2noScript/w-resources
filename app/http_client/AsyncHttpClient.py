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

import asyncio
import httpx
import json
import re
from typing import Optional, Dict, Any
from httpx import Response
from app.http_client.HttpException import (
    APIConnectionError,
    APIResponseError,
    APITimeoutError,
    APIUnavailableError,
    APIUnauthorizedError,
    APINotFoundError,
    APIRateLimitError,
    APIRetryExhaustedError, APIFileDownloadError,
)
from app.utils.logging_utils import configure_logging

# Initialize logger instance
logger = configure_logging(__name__)


class AsyncHttpClient:
    """
    Asynchronous HTTP client
    """

    def __init__(self, proxy_settings: Optional[Dict[str, str]] = None, retry_limit: int = 3,
                 max_connections: int = 50, request_timeout: int = 10, max_concurrent_tasks: int = 50,
                 headers: Optional[Dict[str, str]] = None, base_backoff: float = 1.0, follow_redirects: bool = False):
        """
        Initialize BaseAsyncHttpClient instance

        :param proxy_settings: Optional proxy settings
        :param retry_limit: Maximum number of retries
        :param max_connections: Maximum number of connections
        :param request_timeout: Request timeout in seconds
        :param max_concurrent_tasks: Maximum number of concurrent tasks
        :param headers: Request headers
        :param base_backoff: Base backoff time for retries
        :param follow_redirects: Whether to follow redirects
        """
        self.proxy_settings = proxy_settings if isinstance(proxy_settings, dict) else None
        self.headers = headers or {
            "User-Agent": "Fast-Powerful-Whisper-AI-Services-API/HTTP Client",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Cache-Control": "no-cache",
        }
        self.max_concurrent_tasks = max_concurrent_tasks
        self.semaphore = asyncio.Semaphore(max_concurrent_tasks)
        self.retry_limit = retry_limit
        self.request_timeout = request_timeout
        self.base_backoff = base_backoff

        # Create an independent AsyncClient instance
        self.aclient = httpx.AsyncClient(
            headers=self.headers,
            proxies=self.proxy_settings,
            timeout=httpx.Timeout(request_timeout),
            limits=httpx.Limits(max_connections=max_connections),
            transport=httpx.AsyncHTTPTransport(retries=retry_limit),
            follow_redirects=follow_redirects
        )

    async def fetch_response(self, url: str, **kwargs) -> Response:
        """
        Get raw HTTP response

        :param url: Full URL address
        :param kwargs: Additional parameters for the request
        :return: Raw response object
        """
        return await self.fetch_data('GET', url, **kwargs)

    async def fetch_get_json(self, url: str, **kwargs) -> Dict[str, Any]:
        """
        Send GET request and parse JSON response

        :param url: Full URL address
        :param kwargs: Additional parameters for the request
        :return: Parsed JSON data
        """
        response = await self.fetch_data('GET', url, **kwargs)
        return self.parse_json(response)

    async def fetch_post_json(self, url: str, **kwargs) -> Dict[str, Any]:
        """
        Send POST request and parse JSON response

        :param url: Full URL address
        :param kwargs: Additional parameters for the request
        :return: Parsed JSON data
        """
        response = await self.fetch_data('POST', url, **kwargs)
        return self.parse_json(response)

    async def fetch_data(self, method: str, url: str, **kwargs) -> httpx.Response:
        """
        General request handling method

        :param method: HTTP method (e.g., 'GET', 'POST')
        :param url: Full URL
        :param kwargs: Additional parameters for the request
        :return: Response object
        """
        backoff = self.base_backoff
        for attempt in range(self.retry_limit):
            try:
                # Pass kwargs to aclient.request
                response = await self.aclient.request(
                    method=method,
                    url=url,
                    headers=kwargs.pop("headers", self.headers),
                    **kwargs
                )
                if not response.text.strip() or not response.content:
                    if attempt == self.retry_limit - 1:
                        logger.error(
                            f"Failed after {self.retry_limit} attempts. Status: {response.status_code}, URL: {url}")
                        raise APIRetryExhaustedError()
                    await asyncio.sleep(backoff)
                    backoff *= 2  # Exponential backoff
                    continue
                return response

            except httpx.RequestError as req_err:
                logger.error(f"Request error on {url}: {req_err}", exc_info=True)
                raise APIConnectionError()
            except httpx.HTTPStatusError as http_error:
                self.handle_http_status_error(http_error, url, attempt + 1)

    async def fetch_data_via_head(self, url: str, **kwargs) -> httpx.Response:
        """
        Send HEAD request and get response

        :param url: Full URL address
        :param kwargs: Additional parameters for the request
        :return: Response object
        """
        return await self.fetch_data('HEAD', url, **kwargs)

    async def download_file(self, url: str, save_path: str, chunk_size: int = 1024) -> None:
        """
        Download file to specified path

        :param url: Full URL of the file
        :param save_path: Path to save the downloaded file
        :param chunk_size: Size of each download chunk in bytes
        """
        async with self.semaphore:
            try:
                async with self.aclient.stream("GET", url) as response:
                    response.raise_for_status()
                    with open(save_path, "wb") as file:
                        async for chunk in response.aiter_bytes(chunk_size):
                            file.write(chunk)
                    logger.info(f"File downloaded successfully: {save_path}")
            except (httpx.RequestError, httpx.HTTPStatusError) as error:
                logger.error(f"Failed to download file from {url}: {error}", exc_info=True)
                raise APIFileDownloadError(f"Failed to download file from {url}")

    @staticmethod
    def handle_http_status_error(http_error, url: str, attempt):
        """
        Handle HTTP status error

        :param http_error: HTTP status error object
        :param url: Full URL address
        :param attempt: Current attempt count
        :raises: Specific exception based on HTTP status code
        """
        response = getattr(http_error, "response", None)
        status_code = getattr(response, "status_code", None)

        if not response or not status_code:
            logger.error(f"Unexpected HTTP error: {http_error}, URL: {url}, Attempt: {attempt}", exc_info=True)
            raise APIResponseError()

        error_mapping = {
            404: APINotFoundError(),
            503: APIUnavailableError(),
            408: APITimeoutError(),
            401: APIUnauthorizedError(),
            429: APIRateLimitError(),
        }

        error = error_mapping.get(status_code, APIResponseError(status_code=status_code))

        logger.error(f"HTTP status error {status_code} on attempt {attempt}, URL: {url}")
        raise error

    @staticmethod
    def parse_json(response: Response) -> Dict[str, Any]:
        """
        Parse JSON response object

        :param response: Raw response object
        :return: Parsed JSON data
        """
        if len(response.content) == 0:
            logger.error("Empty response content.")
            raise APIResponseError("Empty response content.")

        try:
            return response.json()
        except json.JSONDecodeError:
            match = re.search(r"\{.*\}", response.text)
            if match:
                try:
                    return json.loads(match.group())
                except json.JSONDecodeError as e:
                    logger.error(f"Failed to parse JSON from {response.url}: {e}", exc_info=True)
                    raise APIResponseError("Failed to parse JSON data.", status_code=response.status_code)
            else:
                logger.error("Invalid JSON format.")
                raise APIResponseError("Invalid JSON format.", status_code=response.status_code)
