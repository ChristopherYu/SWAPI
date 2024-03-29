import os
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture(scope="session")
def api_request_context(
        playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        # We set this header per GitHub guidelines.
        # "Accept": "application/vnd.github.v3+json",
        # Add authorization token to all requests.
        # Assuming personal access token available in the environment.
        # "Authorization": f"token {GITHUB_API_TOKEN}",
    }
    request_context = playwright.request.new_context(
        base_url="https://swapi.dev/", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()
