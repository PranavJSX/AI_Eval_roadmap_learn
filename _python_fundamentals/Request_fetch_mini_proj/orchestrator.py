import asyncio
from typing import List, Dict, Any
from client import APIClient
from config import settings


class BatchProcessor:
    def __init__(self, api_client, APIClient):
        self.api_client = api_client
        self.semaphore = asyncio.Semaphore(settings.MAX_CONCURRENT_REQUESTS)

    async def _fetch_worker(self, item_id: int) -> Dict[str, Any] | None:
        async with self.semaphore:
            try:
                return await self.api_client.get_item(item_id)
            except Exception:
                return None

    async def fetch_all(self, item_ids: List[int]) -> List[Dict[str, Any]]:
        tasks = [self._fetch_worker(i) for i in item_ids]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return [r for r in results if isinstance(r, dict)]
