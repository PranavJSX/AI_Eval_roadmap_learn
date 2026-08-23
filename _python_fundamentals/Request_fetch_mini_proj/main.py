import asyncio
import httpx
from config import settings
from client import APIClient
from orchestrator import BatchProcessor


async def main():
    limits = httpx.Limits(
        max_keepalive_connections=settings.MAX_KEEPALIVE_CONNECTIONS,
        max_connections=settings.MAX_CONCURRENT_REQUESTS * 2,
    )

    async with httpx.AsyncClient(
        base_url=settings.BASE_URL, timeout=settings.TIMEOUT, limits=limits
    ) as http_client:
        api_client = APIClient(http_client)
        processor = BatchProcessor(api_client, APIClient)

        target_ids = list(range(1, 21))  # Fetch items with IDs from 1 to 20
        results = await processor.fetch_all(target_ids)

        print(f"Fetched {len(results)} items successfully.")


if __name__ == "__main__":
    asyncio.run(main())
