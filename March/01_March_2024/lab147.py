import csv

with open("data.csv") as file:
    read = csv.reader(file)
    for i in read:
        print(i[0],i[1],sep="|") 