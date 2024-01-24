import sys
from collections import deque

case=int(sys.stdin.readline())

for i in range(case):
    functionSet = deque(sys.stdin.readline().rstrip())
    length=int(sys.stdin.readline())
    if length==0:
        originList = sys.stdin.readline()
        targetList = deque()
    else:
        originList = sys.stdin.readline().rstrip().strip('[]').split(',')
        targetList = deque(map(int, originList))

    flag=False
    Odd = 0
    R_num = 0


    while(functionSet):
        this_function=functionSet.popleft()
        if this_function=='D':
            if not targetList:
                flag=True
                break
            if Odd:
                targetList.pop()
            else:
                targetList.popleft()
        elif this_function=='R':
            Odd=1-Odd
            R_num+=1

    if Odd:
        targetList.reverse()

    if flag:
        print('error')
    else:
        answer = ','.join((map(str, targetList)))
        print('['+answer+']')



