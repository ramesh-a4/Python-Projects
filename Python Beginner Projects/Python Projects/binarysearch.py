
import random
import time

def navie_search(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i

    return -1

def BinarySearch(l,target,low=None,high=None):
    """
    Binary search uses divide and concour, it divides list into 2 halves and search for the element
    if the target is at midpoint then it returns the index else it divides half list into two halves
    again, division depends on the less than or greater than element.
    """
    if low is None :
        low=0
    if high is None:
        high = len(l)-1
    if high<low:
        return

    midpoint = (low+high)//2
    if l[midpoint]==target:
        return midpoint
    elif target < l[midpoint]:
        return BinarySearch(l,target,low,midpoint-1)
    else:
        return BinarySearch(l,target,midpoint+1,high)

if __name__ == '__main__':
    #creating set to store non identical values
    sorted_list = set()
    length = 1000
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length,3*length))

    sorted_list =  sorted(list(sorted_list))

    #iterate through the sorted list and calculate the time duratation for both
    # navie search and Binary search
    start = time.time()
    #print(start)
    for target in sorted_list:
        navie_search(sorted_list,target)
    end = time.time()
    #print(end)
    interval = (end-start)/length
    print(interval)

    start = time.time()
    for target in sorted_list:
        BinarySearch(sorted_list,target)
    end = time.time()
    interval = (end-start)/length
    print(interval)

