api_response = {
    "first_name" :"pranav",
    "last_name" :"gupta",
    "age" :45,
    "address" :"delhi"
}

print(api_response)
print(api_response.get("age"))
print(api_response.get("address"))
print(len(api_response))
print(api_response["first_name"])

print("******************************************")
for key,value in api_response.items():
    print(key,"-",value)