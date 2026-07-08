from fastapi.testclient import TestClient

from src.app import app


def test_unregister_participant_removes_them_from_activity():
    # Arrange
    client = TestClient(app)
    email = "test@example.com"

    # Act
    signup_response = client.post(f"/activities/Chess Club/signup?email={email}")
    unregister_response = client.delete(
        f"/activities/Chess Club/unregister?email={email}"
    )
    activities = client.get("/activities").json()

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200
    assert email not in activities["Chess Club"]["participants"]
