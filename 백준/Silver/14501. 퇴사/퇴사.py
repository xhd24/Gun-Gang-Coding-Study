import sys

num=int(sys.stdin.readline())
profit=[[0,0] for _ in range(num)]
answer=[]

for i in range(num):
    time, money = map(int, sys.stdin.readline().split())
    if time+i>num:
        profit[i]=[time,0]
    else:
        profit[i]=[time,money]

def dfs(start, total):
    new_start=profit[start][0]
    if start+new_start >= num:
        answer.append(total)
        return
    else:
        for i in range(start+new_start,num):
            dfs(i, total + profit[i][1])

for i in range(num):
    dfs(i,profit[i][1])

print(max(answer))