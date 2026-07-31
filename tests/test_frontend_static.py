from fastapi.testclient import TestClient

from main import app


def test_frontend_shell_served_at_root():
    with TestClient(app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert "CI that" in response.text
    assert "/auth/github/login-url" in response.text
    assert "/runs/dashboard/stats" in response.text
    assert "/static/config.js" in response.text


def test_static_frontend_asset_served():
    with TestClient(app) as client:
        response = client.get("/static/index.html")

    assert response.status_code == 200
    assert "Connect GitHub" in response.text


def test_frontend_origin_regex_setting_defaults_to_none():
    assert settings.frontend_origin_regex is None
