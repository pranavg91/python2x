try:
    with open("TestData.txt","r") as file:
        content= file.read()
        print(content)
except FileNotFoundError as v:
    print(v)
finally:
    print("hello")
    file.close()