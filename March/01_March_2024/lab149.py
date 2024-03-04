import csv

test_data =[

    ['Name','age'],
    ['pranav',30],
    ['Manisha',33]
]

with open("mydata.csv","w") as file:
    writer= csv.writer(file)
    for data in test_data:
        writer.writerow(data)