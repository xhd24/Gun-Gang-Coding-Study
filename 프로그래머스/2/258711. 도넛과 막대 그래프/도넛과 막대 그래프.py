def dfs(v,graph,visited):
    stack=[]
    stack.append(v)
    visited[v]=True
    while stack:
        this_node=stack.pop()
        visited[this_node]=True
        for i in graph[this_node]:
            if visited[i] != True:
                stack.append(i)


def mainPoint (list, graphSet):
    if list.count(False) >=2:
        max=0
        for i in range(1,len(graphSet)):
            if len(graphSet[i])>max:
                max=len(graphSet[i])
                find_point=i
        return find_point
    else:
        find_point=list[1:].index(False)
        return find_point


def find_doubleLoop (graphSet,visited):
    count=0
    for i in range(1,len(graphSet)):
        if len(graphSet[i])==2 and visited[i]==False:
            count+=1
            dfs(i,graphSet,visited)
    return count

def find_line (graphSet,visited):
    count=0
    for i in range(1, len(graphSet)):
        if len(graphSet[i])==0 and visited[i]==False:
             count+=1
    return count

def solution(edges):
    node_num=max(map(max, edges))
    find_point=[False for _ in range(node_num+1)]
    answer = [0,0,0,0]
    visited=[False for _ in range(node_num+1)]
    #make graph
    graphSet = [[] for _ in range(node_num+1)]

    for edge in edges:
        start,end = edge
        find_point[end]=True
        graphSet[start].append(end)
    #find main point
    main_point=mainPoint(find_point,graphSet)
    answer[0]=main_point
    visited[main_point]=True

    #find 8 graph
    answer[3]=find_doubleLoop(graphSet,visited)

    #find line graph
    answer[2]=find_line(graphSet,visited)

    answer[1]=len(graphSet[main_point])-answer[3]-answer[2]

    return answer