#012

# firstNumber = int(input("Enter the first number: "))
# secondNumber = int(input("Enter the second number: "))

# if firstNumber > secondNumber:
#     print(secondNumber, firstNumber)
# else: 
#     print(firstNumber, secondNumber)

#013
# number = int(input("Enter a number less than 20: "))

# if number >= 20:
#     print("Too high")
# else:
#     print("Thank you")

#014
# number = int(input("Enter a number between 10 and 20: "))

# if number >= 10 and number <= 20:
#     print("Thank you")
# else:
#     print("incorrect answer")

#015
# color = input("Enter your favorite color: ")

# if str.lower(color) == "red":
#     print("I like red too")
# else:
#     print("I dont like", color, ", I prefer red")

#016
# isRaining = str.lower(input("Is it raining?\n"))

# if isRaining == "yes":
#     isWindy = str.lower(input("Is it windy?\n"))

#     if isWindy == "yes":
#         print("It is too windy for an umbrella")
#     else:
#         print("Take an umbrella")
# else:
#     print("Enjoy your day")

#017
# age = int(input("How old are you?\n"))

# if age >= 18:
#     print("You can vote.")
# elif age == 17:
#     print("You can learn to drive.")
# elif age == 16:
#     print("You can buy a lottery ticket")
# else:
#     print("You can go Tick-or-Treating")
    
#018
# num = int(input("Enter a number\n"))

# if num < 10:
#     print("Too Low")
# elif num >= 10 and num <= 20:
#     print("Correct")
# else:
#     print("Too High")

#019
num = int(input("Enter 1, 2 or 3:\n"))

if num == 1:
    print("Thank you")
elif num == 2:
    print("Well done")
elif num == 3:
    print("Correct")
else:
    print("Error message")