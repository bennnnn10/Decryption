#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

#Ask what is the name of the user and greetings
print("")
print("My name is Codeperman")
your_name = input("What is your name? ")
print("Nice to meet you! " + your_name + ", be ready!")

print("")
print("Let us start our mission for today!".center(81))

#Ask the user to input the encrypted message
encrypted_message = input(f"\nType or input your encrypted message: ")
decrypted_message = ""

#Count the characters you entered
characters_counter = len(encrypted_message)
print(f"\nThe count of the characters you have entered is", characters_counter)

#Its time to turn the encrypted message to decrypted message
for encrypted in encrypted_message:

#If this symbol "*" is/are in the message, change it to letter a
    if "*" in encrypted:
        decrypted_message += "a"

#If this symbol "&" is/are in the message, change it to letter e
    elif "&" in encrypted:
        decrypted_message += "e"

#If this symbol "#" is/are in the message, change it to letter i
    elif "#" in encrypted:
        decrypted_message += "i"

#If this symbol "+" is/are in the message, change it to letter o
    elif "+" in encrypted:
        decrypted_message += "o"

#If this symbol "!" is/are in the message, change it to letter u
    elif "!" in encrypted:
        decrypted_message += "u"
    else:
        decrypted_message += encrypted

#Print the Outcome
print(f"\nEncrypted Message: " + encrypted_message)
print("Decrypted Message: " + decrypted_message)

#Ask the user if they want to decrypt a message once again
while True:
    print(f"\nDo you want to decrypt other nessage, again?")
    yes_or_no = input("Type YES if you want to continue and NO if you want to exit.")
    if yes_or_no == "YES":
    
    #Ask the user to input the encrypted message
        encrypted_message = input(f"\nType or input your encrypted message: ")
        decrypted_message = ""

#Count the characters you entered
        characters_counter = len(encrypted_message)
        print(f"\nThe count of the characters you have entered is", characters_counter)

#Its time to turn the encrypted message to decrypted message
        for encrypted in encrypted_message:

#If this symbol "*" is/are in the message, change it to letter a
            if "*" in encrypted:
                decrypted_message += "a"

#If this symbol "&" is/are in the message, change it to letter e
            elif "&" in encrypted:
                decrypted_message += "e"

#If this symbol "#" is/are in the message, change it to letter i
            elif "#" in encrypted:
                decrypted_message += "i"

#If this symbol "+" is/are in the message, change it to letter o
            elif "+" in encrypted:
                decrypted_message += "o"

#If this symbol "!" is/are in the message, change it to letter u
            elif "!" in encrypted:
                decrypted_message += "u"
            else:
                decrypted_message += encrypted

#Print the Outcome
        print(f"\nEncrypted Message: " + encrypted_message)
        print("Decrypted Message: " + decrypted_message)

    if yes_or_no == "NO":
        print("Codeperman is leaving.....")
        break