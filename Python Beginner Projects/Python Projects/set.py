# lst=[1,1,1,1,2,2,2,2,3,3,4,4,5,5]
# a=set()
# for i in lst:
#     a.add(i)

# print(list(a))

from importlib_metadata import NullFinder


# lst=[(1,2,3),(4,5,6),()]
# for i in lst:
#     if i==():
#         lst.remove(i)
# print(lst)

# print([x for x in lst if x!=()])

lst=[15,24,33,42,51]
sum=[]
total=0
for i in lst:
    total=0
    num=str(i)
    num=list(num)
    for i in range(len(num)):
        x=int(num[i])
        total+=x

    sum.append(total)

print(sum)
