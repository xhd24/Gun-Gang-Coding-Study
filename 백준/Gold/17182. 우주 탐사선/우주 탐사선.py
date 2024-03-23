import sys
from collections import deque

num, start=map(int,sys.stdin.readline().split())
space=[[0 for _ in range(num)] for _ in range(num)]
queue=deque()
answer=[]

for i in range(num):
    space[i]=list(map(int, sys.stdin.readline().split()))

for i in range(num):
    for j in range(num):
        for k in range(num):
            space[j][k]=min(space[j][k], space[j][i]+space[i][k])

def tracking(start, point):
    for i in range(num):
        if visited[i]==False:
            visited[i] = True
            tracking(i, point+space[start][i])
            visited[i]=False
    if not False in visited:
        answer.append(point)


visited=[False for _ in range(num)]
tracking(start,0)
print(min(answer))
