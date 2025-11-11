numberOne = int(input("Enter first number: "))
numberTwo = int(input("Enter second number: "))

# if (numberOne >= numberTwo):
#     print(numberOne + numberTwo)
# else:
#     print(numberTwo - numberOne)


if numberOne >=100 and numberTwo<=500:
    print(numberOne + numberTwo)
elif numberOne <=0 and numberTwo>=1000:
    print(numberOne - numberTwo)
elif numberOne <=1000 and numberTwo>=0:
    print(numberOne / numberTwo)
else:
    print(numberOne * numberTwo)