#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

#Header design
print("\033[;33;1;3m=\033[0m" * 70)
print("\033[;1;3mHello, I hope you are doing good!\U0001f600\033[0m".center(81))
print("\033[;33;1;3m=\033[0m" * 70)

#Ask what is the name of the user and greetings
print("")
print("\033[1;3mMy name is \033[;96;1;3mCodeperman\033[0m")
your_name = input("\033[1;3mWWhat is your name?\033[0m")
print("\033[;1;3mNice to meet you!\033[;34;1;3m" + your_name + "\033[0m \033[;1;3m, be ready!\033[0m")

print("")
print("\033[;33;1;3m-\033[0m" * 70)
print("\033[;1;3mLet us start our mission for today!\033[0m".center(81))
print("\033[;33;1;3m-\033[0m" * 70)

#Ask the user to input the encrypted message
encrypted_message = input(f"\n\033[33;1;3mType or input your encrypted message: \033[0m")
decrypted_message = ""

#Count the characters you entered
characters_counter = len(encrypted_message)
print(f"\n\033[1mThe count of the characters you have entered is", characters_counter)

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
print(f"\n\033[96;1;3mEncrypted Message: \033[0m" + encrypted_message)
print("\033[96;1;3mDecrypted Message: \033[0m" + decrypted_message)
print("")
print("\033[;33;1;3mMission Accomplished!\033[0m".center(84, "~"))

#Ask the user if they want to decrypt a message once again
while True:
    print(f"\n\033[40m\033[1;3Do you want to decrypt other nessage, again?\033[0m")
    yes_or_no = input("\033[40m\033[1;3mType\033[40m\033[0m \033[40m\033[33;1;3mYES\033[0m \033[40m\033[1;3mif you want to continue and \033[40m\033[0m\033[33;1;3m\033[40mNO\033[0m \033[40m\033[1;3mif you want to exit. \033[0m")
    if yes_or_no == "YES":

    #Header design
        print("")
        print("\033[;36;1;3m=\033[0m" * 70)
        print("\033[;1;3mHello, again!\U0001f600\033[0m".center(81))
        print("\033[;36;1;3m=\033[0m" * 70)
    
    #Ask the user to input the encrypted message
        encrypted_message = input(f"\n\033[33;1;3mType or input your encrypted message: \033[0m")
        decrypted_message = ""

    #Count the characters you entered
        characters_counter = len(encrypted_message)
        print(f"\n\033[1mThe count of the characters you have entered is", characters_counter)

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
        print(f"\n\033[96;1;3mEncrypted Message: \033[0m" + encrypted_message)
        print("\033[96;1;3mDecrypted Message: \033[0m" + decrypted_message)
        print("")
        print("\033[;33;1;3mMission Accomplished!\033[0m".center(84, "~"))

    if yes_or_no == "NO":
        print(f"\n\033[31;1;3mCodeperman is leaving.....")
        break