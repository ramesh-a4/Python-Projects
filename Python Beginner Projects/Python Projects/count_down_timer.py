import time

def Counter(t):
    while t:
        #Loops untill t=0
        mins,secs = divmod(t,60) #divmod(dividend,divisor) function gives quiotent and reminder values in tuple
        print("{:02d}:{:02d}".format(mins,secs),end = "\r")
        time.sleep(1)
        t -= 1

    while t==False:
        mins,secs = divmod(t,60)
        print("{:02d}:{:02d}".format(mins,secs))
        print("Time UP")
        break

t = input("Enter the number of secs")
Counter(int(t))