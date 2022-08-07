#020
# firstName = input("Enter your first name:\n")
# print("Length of your name is", len(firstName))

#021
# firstName = input("Enter your first name:\n")
# surName = input("Enter your surname:\n")

# fullName = firstName + " " + surName

# print(fullName, "Length:", len(fullName))

#022
# fullName = input("Enter your full name in lower case:\n")
# print("Your capitalized full name is", fullName.title())

#023
# firstLineNurseryRhyme = input("Type in the first line of a nursery rhyme:\n")
# print(len(firstLineNurseryRhyme))

# start = int(input("Enter a starting position:\n"))
# end = int(input("Enter ending number:\n"))

# print(firstLineNurseryRhyme[start:end])

#024
# anyWord = input("Enter any word:\n")

# print(anyWord.upper())

#025
# firstName = input("Enter your first name:\n")

# if len(firstName) < 5:
#     lastName = input("Enter your last name:\n")
#     fullName = (firstName + " " + lastName).upper()
#     print(fullName)
# else:
#     print(firstName.lower())

#026
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
word = input("Enter a word:\n")

if word[0] in vowels:
     print(word + "way")
else:
    length = len(word)
    wordWithoutFirstLetter = word[1:length]
    pigEnding = word[0] + "ay"

    print(wordWithoutFirstLetter + pigEnding)