import random
import string
print("welcome to random password generator")
print("-"*36)

#taking the proper input from the user for the length of the password that is to be generated.
while True:
    try:
        length=int(input("Enter the length of the password you want: "))
        break
    except ValueError:
        print(" Your got value error !!! \n You should enter the length in int format")

#asking user if he or she wants special characters in the password
while True:
    print("Do you want special characters in your password")
    choice = input(' if yes type "y or Y"\n if no type "n or N": ')

    if choice=="y" or choice=="Y":
        characters = (string.ascii_letters + string.digits + string.punctuation)
        break


    elif choice=="n"or choice=="N":
        characters = (string.ascii_letters + string.digits)
        break
    else:
        print("Wrong input !!! ")
        choice = input(' if yes type "y"\n if no type "n"')


password =(''.join(random.choices(characters, k=length)))
print(f"your password is: {password}")