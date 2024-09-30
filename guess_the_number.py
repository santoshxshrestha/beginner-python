import random
print ('GET THE CORRECT GUESSING')
random_int = random.randint(0,101)
print("Hey there , Welcome ")

while True:
    try:
        print("-"*40)
        guessed_num = int(input("Guess a number form 'zero' to 'hundred': "))
        if (guessed_num>100 or guessed_num<0):
            print(" invalid input\n please input a number form 'one' to 'hundred'")
            continue
        
        if guessed_num<random_int:
            print("-"*37)
            print("Your guess is too low then the number")
        
        elif guessed_num>random_int:
            print("-"*38)
            print("Your guess is too high then the number")
            
        elif guessed_num==random_int:
            print(f'CONGRATULATION !!!\nyou got the correct guessing "{random_int}"')
            break

    except ValueError:
        print("You got value error !!!")
