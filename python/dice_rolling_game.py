import random

while True:
    choice=input(f"Enter your choice (y/n)").lower()
    if choice=='y':
        die1=random.randint(1,50)
        die2=random.randint(1,50)
        print(f"{die1}",{die2})

    elif choice=='n':
        print("thanks for playing")

    else:
        print("invalid choice")    