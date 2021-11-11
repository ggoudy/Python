word = input("Please enter the word Cyber or Defenders: ")

# Slightly more elegant solution
if str.capitalize(word) == "Cyber":
    print("Welcome Cyber!")
elif str.capitalize(word) == "Defenders":
    print("Welcome Defenders!")
else:
    print("Unauthorized")

# Original solution
'''
if word == "Cyber" or word == "cyber":
    print("Welcome Cyber!")
elif word == "Defenders" or word == "defenders":
    print("Welcome Defenders!")
else:
    print("Unauthorized")
'''

