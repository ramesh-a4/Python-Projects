import random

def play():
    while True:
        choice = input('Enter r for rock, p for paper and s for scissor')
        if choice not in ['r','p','s']:

            if choice=='d':
                break
            else:
                print('Please enter the valid keyword')
                continue
        #if choice == 'd':
            #break

        random_choice=random.choice(['r','p','s'])


        if choice == random_choice:
            print( 'tie')

        elif win_ply(choice,random_choice):
            print( 'You won')

        else:
            print( 'You lost')


    # r<p & p<s and s<r
def win_ply(choice,random_choice):
    if (choice=='r' and random_choice=='s') or (choice == 's'and random_choice=='p') or (choice =='p'and random_choice=='r'):
        return True

play()
