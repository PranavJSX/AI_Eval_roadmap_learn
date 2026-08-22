from dataclasses import dataclass


@dataclass(frozen=True)
class settings:
    BASE_URL: str = "https://jsonplaceholder.typicode.com"
    MAX_CONCURRENT_REQUESTS: int = 5
    TIMEOUT: int = 10  # Timeout in seconds for HTTP requests
    MAX_KEEPALIVE_CONNECTIONS: int = 10  # Maximum number of keep-alive connections


settings = Settings()
