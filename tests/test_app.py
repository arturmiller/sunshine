def test_get_location(api_client):
    response = api_client.get("/location")
    assert response.status_code == 200
    assert response.json() == {
        "latitude": 37.7749,
        "longitude": -122.4194,
        "address": "San Francisco, CA",
    }


def test_get_date(api_client):
    response = api_client.get("/date")
    assert response.status_code == 200
    assert response.json() == {"date": "2023-02-11"}


def test_get_sunrise_sunset(api_client):
    response = api_client.get(
        "/sunrise-sunset?latitude=37.7749&longitude=-122.4194&date=2023-02-11"
    )
    assert response.status_code == 200
    assert "sunrise" in response.json()
    assert "sunset" in response.json()
