def password_generator():
 
 print("smart password generator")
 import random
 import string
 length=int(input("Enter the length of the password: "))
 if length<6:
    print("Password length should be at least 6 characters.")
    return
 include_digits = input("Include digits? (y/n): ").lower() == 'y'
 include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

 characters = string.ascii_letters

 if include_digits:
        characters += string.digits
 if include_symbols:
        characters += string.punctuation
 passowrd="".join(random.choice(characters) for i in range(length))
 print("Your password is: ",passowrd)

password_generator()