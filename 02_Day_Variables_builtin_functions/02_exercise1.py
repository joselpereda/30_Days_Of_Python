import math 

print('Day 2: 30 Days of python programming')
firstName = 'Jose'
lastName = 'Pereda'
fullName = firstName + ' ' + lastName
Country = 'USA'
City = 'San Diego'
Age = 49
isMarried = True
isTrue = True
isLightOn = isTrue
hasChildren, isMale, isTall = True, True, True

#Exercise #1
print('firstName: ', type(firstName))
print('lastName: ', type(lastName))
print('fullName: ', type(fullName))
print('Country: ', type(Country))
print('Age: ', type(Age))
print('isMarried: ', type(isMarried))
print('isTrue: ', type(isTrue))
print('hasChildren: ', type(hasChildren))
print('isMale: ', type(isMale))
print('isTall: ', type(isTall))

#Exercise #s 2 & 3
print('Length of first name is ' + str(len(firstName)) + ' ,while length of last name is ' + str(len(lastName)))
print("_" * 80)

#Exercise #4
#CALCULATE
numOne, numTwo = 5, 4
sum = numTwo + numOne
Diff = numTwo - numOne
Product = numOne * numTwo
Divide = numOne / numTwo
Mod = numTwo % numOne
Power = numOne ^ numTwo
floorDiv = numOne // numTwo

#PRINT TO SCREEN
print("First Number: ", numOne)
print("Second Number: ", numTwo)
print("SUM = ", str(sum))
print("DIFF = ", str(Diff))
print("PRODUCT = ", str(Product))
print("Quotient = ", str(Divide))
print("Modulus = ", str(Mod))
print("Exponent = ", str(Power))
print("Floor Div = ", str(floorDiv))
print("_" * 80)

#Exercise #5
Radius = 30
Radius= int(input("Enter Radius of circle: "))
areaOfCircle = math.pi * Radius ** 2
circOfCircle = 2 * math.pi * Radius

print("Area of Circle: ", round(areaOfCircle,2), " meters sqr")
print("Circumfrence of Circle: ", round(circOfCircle,2), " meters")

