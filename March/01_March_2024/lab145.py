with open("td.txt","r") as file:
    content =  file.readlines()


for line in content:
    print(line, end=" ")

with open("td.txt","a") as file:
    file.write("\n Pranav11")