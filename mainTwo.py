found = None
for i in "Hello":
    if i == "l":
        found = True
        break
else:
    found = False
print(found)

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