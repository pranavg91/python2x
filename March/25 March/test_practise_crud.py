import allure
import pytest
import requests

def token():
    base_url ="https://restful-booker.herokuapp.com"
    base_path ="/auth"
    POST_URL= base_url +base_path

    headers ={
        "Content_Type" :"application/json"
    }
    payload ={
        "username" : "admin",
        "password" : "password123"
    }
    response=requests.post(url=POST_URL,headers=headers,json=payload)
    response_json = response.json()
    token = response_json["token"]
    assert token is not None
    return token


def create_booking():
    url="https://restful-booker.herokuapp.com/booking"
    headers ={
        "Content-Type" :"application/json"
    }
    payload={
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

    response=requests.post(url=url,headers=headers,json=payload)
    assert response.status_code ==200
    response_booking = response.json()
    booking_id = response_booking["bookingid"]
    return booking_id

def test_put():
    base_url_path ="https://restful-booker.herokuapp.com/booking/"
    param = create_booking()
    PUT_URL = base_url_path + str(param)
    cookie = "token=" + token()
    print(cookie)
    headers ={
        "Content-Type":"application/json",
        "cookie" : cookie
    }
    payload ={
        "firstname" : "James",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
            "additionalneeds" : "Breakfast"
    }

    response = requests.put(url=PUT_URL,headers=headers,json=payload)
    assert response.status_code == 200