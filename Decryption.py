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
#If this symbol "*" is/are in the message, change it to letter a
#If this symbol "&" is/are in the message, change it to letter e
#If this symbol "#" is/are in the message, change it to letter i
#If this symbol "+" is/are in the message, change it to letter o
#If this symbol "!" is/are in the message, change it to letter u
#Print the Outcome