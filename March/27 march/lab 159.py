import requests

from conftest import create_token,create_booking
def test_put(create_booking,create_token):
    base_url_path ="https://restful-booker.herokuapp.com/booking/"
    param = create_booking
    PUT_URL = base_url_path + str(param)
    cookie = "token=" + create_token
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