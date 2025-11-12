country = {
    "name": "Kazakhstan",
    "language": "Kazakh"
}
print(country["name"])
print(country["language"])

persons = {
    "user_1":{
        "first_name": "Mike",
        "last_name": "Smith",
        "email": "mike.smith@gmail.com",
        "age": 25,
        "address": ("Kazakhstan","Almaty", "Samanova", "50", "100")
    },
    "user_2":{
        "first_name": "John",
        "last_name": "Ronaldo",
        "email": "john.ronaldo@gmail.com",
        "age": 50,
        "address": ("Kazakhstan","Astana", "Salamorova", "100", "45")
    }
}
print(persons["user_1"]["address"][2])