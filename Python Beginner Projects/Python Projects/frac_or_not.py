import re

def check(x):
    #clearing spaces
    lef=0
    rig=len(x)-1
    for i in range(len(x)):
        if x[i]!=' ':
            lef=i
            break
    for j in range(len(x)-1,0,-1):
        if x[j]!=' ':
            rig=j
            break

    if lef>rig:
        return False #checking index value of lef and rig if lef is greater than the reg then return False

    if lef==rig and not (x[lef]>='0' and x[lef]<='9'):
        return False #if lef and reg are equal then checking the value at the index if it is not
                        #in closed interval then return False

    if lef<rig and not (x[lef]=='e' or x[lef]=='.'or (x[lef]>=
        '0' and x[lef]<='9')):
        return False

    if x[lef]=='e' and x[lef+1] !='.':
        return False

    for i in range(lef,rig+1):
        if (x[i]!='e'and x[i]!='.'and not (x[i]>='0'and x[i]<='9' )):
            return False

        if x[i]=='.':
            if i==rig:
                return True

            if (not(x[i+1]>='0' and x[i+1]<='9')):
                return False

        if x[i]=='e':
            if i==rig:
                return True

            if x[i+1]!='.':
                return False


    return True

    

if __name__ == '__main__':
    x=input("Enter the value to check")
    value=check(x)
    if value==True:
        print("Enter string is valid fraction number")
    else:
        print('Entered string value is not valid fraction number')

