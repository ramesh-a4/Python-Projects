import random

def computer_guess(x):
    guess_num = int(input('Enter the guessing number'))
    random_num=0
    while guess_num != random_num:
        random_num=random.randint(1,x)
        #y=input()
        if random_num < guess_num:
            print(f'sorry, {random_num} number is too low')
            
        elif random_num > guess_num:
            print(f'sorry, {random_num} number is too high')
            x -=1


    print('yeah, computer guessed the correct number {}'.format(random_num))


computer_guess(10)