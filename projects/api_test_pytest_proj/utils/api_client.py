import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint, params=None):
        return self.session.get(f"{self.base_url}{endpoint}", params=params)

    def post(self, endpoint, payload=None):
        return self.session.post(f"{self.base_url}{endpoint}", json=payload)

    def delete(self, endpoint):
        return self.session.delete(f"{self.base_url}{endpoint}")