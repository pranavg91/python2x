import allure
import pytest
import requests


@allure.title("Testing")
@allure.description("TC1 test create booking")
@allure.label("owner","Pranav")

def test_create_booking():

    url ="https://restful-booker.herokuapp.com/booking"
    headers ={
        "Content-Type":"application/json"
    }
    payload ={
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
        "additionalneeds" : "Breakfast"
    }

    response = requests.post(url=url,headers=headers,json=payload)
    response_json = response.json()
    firstname = response_json["booking"]["firstname"]
    assert firstname == "Jim"
    assert response.status_code == 200
    assert response_json["bookingid"] is not None