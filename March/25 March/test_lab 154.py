import requests
import pytest
import allure


@allure.title("create booking")
@allure.description("TC1 - Verify the create booking")
@pytest.mark.crud
def test_create_booking_postive():
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
    print(response_json)
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int
    firstname =response_json["booking"]["firstname"]
    assert firstname == "Jim"
    lastname =response_json["booking"]["lastname"]
    assert lastname == "Brown"
    checkin_date = response_json["booking"]["bookingdates"]["checkin"]
    assert checkin_date == "2018-01-01"

@allure.title("create booking")
@allure.description("TC2 - Verify the create booking is not created ")
@pytest.mark.crud
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {
        "Content-Type": "application/json"
    }
    payload = {}
    response = requests.post(url=URL, headers=headers, json=payload)
    print(type(URL))
    assert response.status_code == 500
