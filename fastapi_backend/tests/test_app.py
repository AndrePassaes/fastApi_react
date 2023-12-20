import pytest

from httpx import AsyncClient
from fastapi_backend.app import app


HAPPY_PATH_ID = "happy_path"
EDGE_CASE_ID = "edge_case"
ERROR_CASE_ID = "error_case"

@pytest.mark.parametrize(
    "test_id, expected_status, expected_body",
    [
        (HAPPY_PATH_ID, 200, {"body": "primeira integração de back e front"}),
    ]
)
@pytest.mark.asyncio
async def test_get_data(test_id, expected_status, expected_body):
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/get_data")
        
        assert response.status_code == expected_status
        assert response. json() == expected_body
