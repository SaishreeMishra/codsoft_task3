# A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a
# password generator application using Python, allowing users to specify the length and complexity of the password.
# User Input: Prompt the user to specify the desired length of the password.
# Generate Password: Use a combination of random characters to generate a password of the specified length.
# Display the Password: Print the generated password on the screen.

import random
def Password_Generator(length):

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

    if length<=0:
        return "password length must be greater than 0"

    password = ""   

    for index in range(length):
        password = password + random.choice(chars)

    return password

while True:
    print("""Options:
    1. Generate Password
    2. Exit""")
    
    choice=int(input("Enter your choice: "))
    if choice==1:
        try:
            password_len=int(input("Enter your Password Length: "))
            password= Password_Generator(password_len)
            print("Password: ",password)
            
        except ValueError:
            print("Invalid Input. Please enter a valid password length.")
    
    elif choice==2:
        print("Exiting the Random Password Generator")
        break
    else:
        print("Invalid choice")