import sys
from collections import deque

ladder, snake = map(int, sys.stdin.readline().split())
visited=[False for _ in range(100+1)]
queue=deque()
times=0
gameMap=[0 for i in range(100+1)]
dict={}

for i in range(ladder + snake):
    start, end = map(int, sys.stdin.readline().split())
    dict[start]=end

queue.append([1,0])

while queue:
    this_node,time = queue.popleft()
    if this_node>=100:
        print(time)
        break
    if not visited[this_node]:
        visited[this_node] = True
        time+=1
        for i in range(1,7):
            next_node=this_node+i
            if next_node in dict:
                queue.append([dict[next_node],time])
            else:
                queue.append([next_node, time])
