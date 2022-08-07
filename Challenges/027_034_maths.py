import math
#027
# bigDecimal = float(input("Enter a number with a lot of decimal points:\n"))
# product = bigDecimal * 2
# print(product)

#028
# bigDecimal = float(input("Enter a number with a lot of decimal points:\n"))
# product = bigDecimal * 2
# print(round(product, 2))

#029
# import math
# number = int(input("Enter a number over 500:\n"))
# squareRoot = math.sqrt(number)
# print(round(squareRoot, 2))

#030
# import math
# print(round(math.pi, 5))

#031
# import math
# radius = float(input("Enter the radius of a circle:\n"))
# area = math.pi * (radius ** 2)
# print("The area of the circle is", area)

#032
# radius = float(input("Enter the radius of the cylinder:\n"))
# depth = float(input("Enter the depth of the cylinder:\n"))

# area = math.pi * (radius ** 2)
# volume = area * depth
# print("The volumne of the cylinder is", round(volume, 3))

#033
# num1 = int(input("Enter number 1:\n"))
# num2 = int(input("Enter number 2:\n"))

# quotient = num1 // num2
# remainder = num1 % num2

# print(num1, "divided by", num2, "is", quotient, "with", remainder, "remaining")

#034
print("1) Square\n2) Triangle\n")
number = int(input("Enter a number:\n"))

if number == 1:
    length = float(input("Enter the length of one of its sides:\n"))
    area = length ** 2
    print("The area of the square is", area)
elif number == 2:
    base = float(input("Enter the base:\n"))
    height = float(input("Enter the height:\n"))
    area = .5 * base * height
    print("The area of the triangle is", area)
else:
    print("Please enter and appropriate value")