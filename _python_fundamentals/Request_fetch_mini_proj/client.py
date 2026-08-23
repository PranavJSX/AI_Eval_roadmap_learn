import httpx
from typing import Any, Dict


class APIClient:
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def get_item(self, item_id: int) -> Dict[str, Any]:
        try:
            response = await self.client.get(f"/posts/{item_id}")
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()
        except httpx.HTTPStatusError as exc:
            print(f"[ERROR {exc.response.status_code}] Failed to fetch item {item_id}")
            raise
        except httpx.RequestError as exc:
            print(f"[ERROR] An error occurred while requesting {exc.request.url!r}.")
            raise
