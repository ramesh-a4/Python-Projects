import random

def guess(x):
    random_num=random.randint(1,x)
    gue=0
    while gue != random_num :
        gue=int(input('Enter the guessing number between 1 and {}'.format(x)))
        if gue < random_num:
            print('number is too low')
        elif gue > random_num:
            print("number is too large")

    print('Yeah, you guess the correct number')






if __name__ =='__main__':
    x= int(input("Enter the number"))
    guess(x)