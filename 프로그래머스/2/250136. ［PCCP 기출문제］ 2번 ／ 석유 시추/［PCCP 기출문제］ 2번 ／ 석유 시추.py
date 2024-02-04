from collections import deque

def solution(land):
    answer = 0

    m = len(land[0])
    n = len(land)
    index = -1
    stack = []
    queue=deque()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    size_dic={}
    visited=[]


    for column in range(m):
        sum=0
        for i in range(len(visited)):
            visited[i]=False
        for row in range(n):
            if land[row][column] == 1:
                queue.append((column, row))
                land[row][column]=index
                count = 1
                while queue:
                    x, y = queue.popleft()

                    for i in range(4):
                        nx = dx[i] + x
                        ny = dy[i] + y
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        if land[ny][nx] == 1:
                            queue.append((nx, ny))
                            land[ny][nx] = index
                            count += 1

                size_dic[index] = count
                visited.append(True)
                index=index-1
                sum+=count

            if land[row][column]<0 and not visited[abs(land[row][column])-1]:
                sum+=size_dic[land[row][column]]
                visited[abs(land[row][column])-1]=True

        if sum>answer:
            answer=sum

    return answer