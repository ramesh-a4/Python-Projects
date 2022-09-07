
import re
c = 0
count = 0
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    lst = re.findall('^From .* ([0-9]+)',line)
        #print(line)
    if len(lst) > 0:
        a = lst[0]
        b = int(a)
        c = c + b
        count += 1 
print(c)
print(count)
print(c/count)


'''
x = 'the cost my laptop is $8000 '
lst = re.search('\$[0-9]+', x)
print(lst)
'''
'''
a=0
for i in range(0,9):
    a = a +i
    print(a)
print(a)
'''