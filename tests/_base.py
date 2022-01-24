from fastapi.testclient import TestClient

from core import create_app

app = create_app()

client = TestClient(app, base_url="http://127.0.0.1:5000")

