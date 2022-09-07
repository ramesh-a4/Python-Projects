import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,<?/;:'!@#$%^&*"

print("Welcome to password generator")

n = int(input("Enter the number of characters should be present in the password"))
m = int(input("Enter the number of passwords you want"))

while m>0:
    length = n
    while length>0:
        print(random.choice(chars),end="")
        length -=1
    print('')
    m -=1
    
