print("Welcome to the simple calculator")
print("\n")

print("select an operation to perform")
print('-'*30)
print(" 1.ADD \n 2.SUBTRACT \n 3.MULTIPLY \n 4.DIVIDE")
while True:
    try:
        operation = int(input("Select an operation from above (1-4): "))
        if operation < 1 or operation > 4:
            print("Invalid selection, please select a valid operation.")
            continue
        break  # Exit loop once a valid operation is chosen
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")

num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))

if operation==1:
    print(f"sum of two numbers '{num1}' and '{num2}' is: ", num1 + num2)
elif operation==2:
    print(f"subtraction of two numbers '{num2}' from '{num1}' is: ",num1 - num2)
elif operation==3:
    print(f"product of two numbers '{num1}' and '{num2}' is: ",num1 * num2)
elif operation==4:
    try:
        print(f"division of two numbers '{num1}' by '{num2}' is: ",num1 / num2)
    except ZeroDivisionError:
         print("invalid input, you got zero division error!!!")