from fastapi.testclient import TestClient

from main import app


def test_frontend_shell_served_at_root():
    with TestClient(app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert "CI that" in response.text
    assert "/auth/github/login-url" in response.text
    assert "/runs/dashboard/stats" in response.text


def test_static_frontend_asset_served():
    with TestClient(app) as client:
        response = client.get("/static/index.html")

    assert response.status_code == 200
    assert "Connect GitHub" in response.text
