import random


min_value = 1
max_value = 6

role = "yes"

while role == "YES" or role == "yes" or role=="y":
    number= random.randint(min_value,max_value)
    print(number)

    role = input("Do you want to role the dice again,if yes type'yes or y' else 'no or n' to terminate")

else:
    if role == "NO" or role == "no" or role == "n":
        print("You terminated the roling")
    else:
        print("Please enter the valid input")


