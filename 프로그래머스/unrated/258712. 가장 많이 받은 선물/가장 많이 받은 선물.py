def solution(friends, gifts):
    answer = 0
    array = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    visited = [[2 for _ in range(len(friends))] for _ in range(len(friends))]
    credit = [0 for _ in range(len(friends))]

    for i in gifts:
        a, b = i.split(' ')
        array[friends.index(a)][friends.index(b)] += 1

    for i in array:
        print(i)
        print()
        
    for i in range(len(friends)):
        visited[i][i] = 0

    for i in range(len(friends)):
        for j in range(len(friends)):
            credit[i] += array[i][j] - array[j][i]

    for i in range(len(friends)):
        for j in range(len(friends)):
            if visited[i][j] == 2:
                if array[i][j] > array[j][i]:
                    visited[i][j] = 1
                    visited[j][i]=0
                elif array[i][j] < array[j][i]:
                    visited[j][i] = 1
                    visited[i][j]=0
                else:
                    if credit[i]>credit[j]:
                        visited[i][j]=1
                        visited[j][i] = 0
                    elif credit[i]<credit[j]:
                        visited[j][i]=1
                        visited[i][j] = 0
                    else:
                        visited[i][j]=0
                        visited[j][i] = 0

    for i in visited:
        if sum(i)>answer:
            answer=sum(i)
                    
    return answer