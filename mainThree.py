try:
    with open("text.txt", "r", encoding="utf-8") as file:
        file.read()
except FileNotFoundError:
    print("File not found.")
data = input("Enter your text : ")

file = open("text.txt","w")
file.close()

# file.close()
# print(file.read())
# for line in file:
#     print(line, end="")

# n = int(input("Enter length of list : "))
# userList = []
# index = 0
# while index < n:
#     string = "Enter element #" + str(index + 1)+ ": "
#     userList.append(int(input(string)))
#     index += 1
# print(userList)
#
# number = 0
# while number == 0:
#     try:
#         number = int(input("Enter a number: "))
#         number += 5
#         print(number)
#     except ValueError:
#         print("That's not a number")






# def test_minimal(listNumbers):
#     minNumber = listNumbers[0]
#     for element in listNumbers:
#         if element < minNumber:
#             minNumber = element
#
#     return minNumber
#
#
# nums1 = [100, 9, 70, 80, 1000]
# nums2 = [10, 90, 700, 30, 10]
# minNumber1 = test_minimal(nums1)
# minNumber2 = test_minimal(nums2)
# # print(test_minimal(nums1))
# # print(test_minimal(nums2))
# if minNumber1 > minNumber2:
#     print(minNumber2)
# else:
#     print(minNumber1)

# data = {50, 6, 30, 60, True, 30}
# data.add(32)
# data.update(["32", False, 7, 9])
# data.remove(True)
# print(data)
# data.pop()
# print(data)
# new_data = frozenset([100, 500, 376, 5, 100, True, 500])
# print(new_data)
#
# word = "Hello"
# newTuple = set(word)
# print(newTuple)



# country = {
#     "name": "Kazakhstan",
#     "language": "Kazakh"
# }
# print(country["name"])
# print(country["language"])
#
# persons = {
#     "user_1":{
#         "first_name": "Mike",
#         "last_name": "Smith",
#         "email": "mike.smith@gmail.com",
#         "age": 25,
#         "address": ("Kazakhstan","Almaty", "Samanova", "50", "100")
#     },
#     "user_2":{
#         "first_name": "John",
#         "last_name": "Ronaldo",
#         "email": "john.ronaldo@gmail.com",
#         "age": 50,
#         "address": ("Kazakhstan","Astana", "Salamorova", "100", "45")
#     }
# }
# print(persons["user_1"]["address"][2])