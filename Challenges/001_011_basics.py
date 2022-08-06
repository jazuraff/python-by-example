# 001
# Ask for the user’s first name and
# display the output message
# Hello [First Name]

# firstName = input("Enter your first name")
# print("Hello", firstName)

# 002
# Ask for the user’s first name and then ask for
# their surname and display the output message Hello [First Name] [Surname]
# firstName = input("Enter your first name: ")
# surName = input("Enter your surname: ")
# print("Hello ", firstName, surName)


# 003
# Write code that will display the joke “What do you call a bear with no
# teeth?” and on the next line display the answer “A gummy bear!” Try to
# create it using only one line of code.

# print("What do you call a bear with now teeth?\nA gummy bear!")

# 004
# Ask the user to enter two numbers. Add them together and
# display the answer as The total is [answer].

# firstNum = int(input("Enter a number: "))
# secondNum = int(input("Enter a second number: "))
# sum = firstNum + secondNum
# print("The total is ", sum)

# 005
# Ask the user to enter three numbers. Add together the first
# two numbers and then multiply this total by the third. 
# Display the answer as The answer is [answer]

# firstNum = int(input("Enter a number: "))
# secondNum = int(input("Enter a second number: "))
# thirdNum = int(input("Enter a third number: "))
# sum = (firstNum + secondNum) * thirdNum
# print("The answer is ", sum)

# 006
# Ask how many slices of pizza the user started with and ask
# how many slices they have eaten. Work out how many slices they have left
# and display the answer in a userfriendly format.

# startingSlices = int(input("How many slices of pizza did you begin with: "))
# eatenSlices = int(input("How many slices of pizza have you eaten: "))
# slicesLeft = startingSlices - eatenSlices
# print("You have", slicesLeft, "pizza slices left")

# 007
# Ask the user for their name and their age. Add 1 to their age
# and display the output [Name] next birthday you will be [new age].

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(name, "next birthday you will be", age + 1)

# 008
# Ask for the total price of the bill, then ask how
# many diners there are. Divide the total bill by the
# number of diners and show how much each person must pay.

# totalBill = int(input("What is the total price of the bill: "))
# dinersCount = int(input("How many diners: "))
# splitAmount = totalBill / dinersCount
# print("Each person must pay $", splitAmount)

# 009
# Write a program that will ask for a number of days and then will show how many
#  hours, minutes and seconds are in that number of days.

# days = int(input("Enter a number of days: "))
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# print("In", days, "days, there are:\n", hours, "Hours\n", minutes, "Minutes\n", seconds, "Seconds")

# 010
# There are 2,204 pounds in a kilogram. Ask the
# user to enter a weight in kilograms and convert it to pounds.

# kilograms = int(input("Enter a weight in kilograms: "))
# pounds = 2.204 * kilograms
# print("The weight in pounds is", pounds)

# 011
# Task the user to enter a number over 100 and then enter a number under
# 10 and tell them how many times the smaller number goes into the larger
# number in a user-friendly format.

from cgitb import small


largeNum = int(input("Enter a number over 100: "))
smallNum = int(input("Enter a number under 10: "))
quotient = largeNum // smallNum
mod = largeNum % smallNum

print(smallNum, "goes into", largeNum, quotient, "times")

if mod > 0:
    print("with an amount of", mod, "leftover")
