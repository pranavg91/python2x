import pytest
import requests

@pytest.fixture()
def create_token():

    url="https://restful-booker.herokuapp.com/auth"

    headers = {
        "Content-Type": "application/json"
    }
    payload ={
        "username" : "admin",
        "password" : "password123"
    }

    response=requests.post(url=url,headers=headers,json=payload)
    response_json = response.json()
    assert response.status_code == 200
    token = response_json["token"]
    assert token is not None
    print(token)
    return token

@pytest.fixture()
def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"

    URL = base_url + base_path

    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload)

    assert response.status_code == 200
    response_json = response.json()
    booking_id = response_json["bookingid"]
    return booking_id
