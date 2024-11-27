import random

usernum = int(input("Enter a number : "))
compnum = random.randint(1,11)

for i in range (0,5):
    if usernum == compnum:
        print("well done you did it !!")
        break

    else :
        usernum = int(input("Enter a number : "))