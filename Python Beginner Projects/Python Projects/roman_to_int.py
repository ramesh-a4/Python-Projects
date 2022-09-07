def Roman(rnum):
    s1=0
    i=0
    s2=0
    inum=0
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    while(i<len(rnum)):
        s1 = d[rnum[i]]
        if i+1<len(rnum):
            s2 = d[rnum[i+1]]
            if(s1>=s2):
                inum = inum+s1
                i = i+1
            else:
                inum = inum + s2-s1
                i = i+2
            
        else:
            inum = inum+s1
            i = i+1

    return inum

if __name__ == '__main__':
    rnum = input("Enter the roman number").upper()
    #rnum = num.upper()
    inum = Roman(rnum)
    print(inum)

