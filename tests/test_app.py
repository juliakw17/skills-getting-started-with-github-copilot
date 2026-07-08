from fastapi.testclient import TestClient

from src.app import app


def test_unregister_participant_removes_them_from_activity():
    client = TestClient(app)

    signup_response = client.post(
        "/activities/Chess Club/signup?email=test@example.com"
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        "/activities/Chess Club/unregister?email=test@example.com"
    )
    assert unregister_response.status_code == 200

    activities = client.get("/activities").json()
    assert "test@example.com" not in activities["Chess Club"]["participants"]
