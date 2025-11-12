word = "Arsenal, manchester, fulham"
land = word.split(", ")
print(land)
for index in range(len(land)):
    land[index] = land[index].capitalize()
print(land)
# n = int(input("Enter length of list : "))
# userList = []
# index = 0
# while index < n:
#     string = "Enter element #" + str(index + 1)+ ": "
#     userList.append(input(string))
#     index += 1
# print(userList)

# listNumbers = [100, 600, 400, 300, 200, True]
#
# for element in listNumbers:
#     print(element)
# listNumbers.pop(1)
# listNumbers.sort()
# listNumbers.remove(600)
# listNumbers.remove(True)
# listNumbers.append(False)
# file = [200, 900, 800]
# listNumbers.extend(file)
# print(listNumbers)
# listNumbers.insert(1, "Hello")
# print(listNumbers)
# print(type(listNumbers[5]))
# print(max(listNumbers))
# print(min(listNumbers))
# print(len(listNumbers))
# print(listNumbers[0])
# for number in listNumbers:
#     print(number)

# found = None
# for i in "Hello World!":
#     if i == "w":
#         found = True
#         break
# else:
#     found = False
# print(found)

# index = 10
# while index <= 20:
#     index += 2
#     print(index)
# for i in range(1, 10, 3):
#     print(i)
# word = "Hello World"
# for letter in word:
#     print(letter.capitalize()*2)


# data = input("Enter your word: ")
# numberOne = 5 if data == "Five" else 0
# print(numberOne)
# numberOne = int(input("Enter first number: "))
# numberTwo = int(input("Enter second number: "))

# if (numberOne >= numberTwo):
#     print(numberOne + numberTwo)
# else:
#     print(numberTwo - numberOne)


# if numberOne >=100 and numberTwo<=500:
#     print(numberOne + numberTwo)
# elif numberOne <=0 and numberTwo>=1000:
#     print(numberOne - numberTwo)
# elif numberOne <=1000 and numberTwo>=0:
#     print(numberOne / numberTwo)
# else:
#     print(numberOne * numberTwo)