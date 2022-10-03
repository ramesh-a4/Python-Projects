
import re
#Email and phone number number masking
f_hand=open('Mbox-Short.Txt')
# count=0
for line in f_hand:
    if line.startswith('From'):
        res=re.search(r'\w+([\.-]?\w)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',line,re.IGNORECASE)
        print(res)

# print(count)


#Phone number masking
number='7338324745'
phone=re.search('\w([0-9\s]+)',number)
if phone:
    print('{}########{}{}'.format(number[0],number[-2],number[-1]))



