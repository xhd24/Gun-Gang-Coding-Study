def solution(n, w, num):
    answer = 0

    floor = n // w
    if n%w ==0:
        blank=0
    else:
        blank=(floor+1)*w-n

    line=[]
    idx=1
    while(len(line)<w):
        line.append(idx)
        idx+=2

    increment = []
    increment.append(line)
    increment.append(list(reversed(line)))

    print(increment)
    idx=num
    floor = (idx-1)//w
    selectInc = 0 if floor%2==1 else 0
    if selectInc == 0:
        column_n= -(num%w)
    else:
        column_n=(num-1)%w


    while(True):
        idx+=increment[selectInc][column_n]
        selectInc=(selectInc+1)%2
        if(idx<=n):
            answer+=1
        else:
            break

    return answer+1