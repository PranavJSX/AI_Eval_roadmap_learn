## Pytest api automation framework

- Contains validations for get, posts and delete requests
- Contains validation for response body, lists and status code validations

### Folder structure

```api_test_project/
├── pytest.ini # Pytest configurations (markers, base settings)
├── conftest.py # Shared fixtures (base URL, API clients, sample payloads)
├── utils/
│ └── api_client.py # Wrapper class around `requests` for cleaner calls
└── tests/
├── test_posts.py # Test suite for /posts endpoints
└── test_users.py # Test suite for /users endpoints
```

### Steps to run

From root directory \
`pytest ` \
`pytest -m`
