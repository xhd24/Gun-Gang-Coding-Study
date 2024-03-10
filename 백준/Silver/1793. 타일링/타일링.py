import sys

while True:
    try:
        size=list(map(int,sys.stdin.readline().split()))
        max_val=max(size)
        answer_list=[0 for _ in range(251)]
        answer=[]

        answer_list[0]=1
        answer_list[1]=1
        answer_list[2]=3

        for i in range(3, 251):
            answer_list[i]=2**i-answer_list[i-1]

        for i in size:
            print(answer_list[i])
    except:
        break