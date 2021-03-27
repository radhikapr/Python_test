#Find max number of a given number by inserting 5 into it
#eg: N=-999 result = -59999
#eg: N=670 result = 675
#eg: N=0    result =50
import math
m =0
def solution(N):
    digits = getdigits(N)
    print(digits)
    m=chkmax(digits,N)
    max_num = int(m)
    if N < 0:
        return (-abs(max_num))
    else:
        return max_num
    pass

#find number of digits in given number
def getdigits(N):
    if N > 0:
        return int(math.log10(N))+1
    elif N == 0:
        return 1
    else:
        return int(math.log10(-N))+1

#find max number
def chkmax(limit,N):
    if N<0:
        flag =1
    else:
        flag =0
    digit=str(abs(N))
    A = [int(d) for d in digit]
    print(A)
    for i in A:
        if (i <= 5 and flag == 0) or (i > 5 and flag == 1):
            A.insert(A.index(i),5)
            break
    print(A)
    m=str()
    for i in A:
        m = m+str(i)
    
    return str(m)