
import pytest
import requests

def test_getmethod():
   response = requests.get("https://restful-booker.herokuapp.com/booking ")
   response_status = response.status_code
   print(response.text)
   print(response.content)
   print(response.headers)
   print(response.url)
   print(response.cookies)

   assert response_status == 200