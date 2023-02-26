import os
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext


# ...

def test_get_all_apis(api_request_context: APIRequestContext) -> None:
    # vehicles_url = "vehicles/"
    res = api_request_context.get(f"/api/")
    content = res.json()
    assert res.ok
