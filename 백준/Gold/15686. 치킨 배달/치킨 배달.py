import sys

map_size, storeN = map(int, sys.stdin.readline().split())
basic_map=[[0 for _ in range(map_size)] for _ in range(map_size)]
house_list=[]
store_list=[]

for i in range(map_size):
    basic_map[i]=list(map(int,sys.stdin.readline().split()))

for i in range(map_size):
    for j in range(map_size):
        if basic_map[i][j]==1:
            house_list.append((i,j))
        elif basic_map[i][j]==2:
            store_list.append((i,j))

def combination(arr,n):
    result=[]
    if n==0:
        return [[]]

    for i in range(len(arr)):
        elem=arr[i]
        for rest in combination(arr[i+1:],n-1):
            result.append([elem]+rest)
    return result

distance_list=[]
for store_list in combination(store_list,storeN):
    distance=0
    for house in house_list:
        best_store=2*map_size
        house_x, house_y = house
        for store in store_list:
            store_x,store_y=store
            if abs(store_x-house_x)+abs(store_y-house_y) < best_store:
                best_store=abs(store_x-house_x)+abs(store_y-house_y)
        distance+=best_store
    distance_list.append(distance)

print(min(distance_list))