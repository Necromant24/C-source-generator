import json



with open("data2.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    cities = []
    for i in data:

        cities.append(i['city'])

    print(cities)

    with open("russian_cities4.json","w") as file2:
        json.dump(cities,file2)


