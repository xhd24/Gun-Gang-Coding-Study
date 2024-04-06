import sys

fruit=int(sys.stdin.readline())
farm={1:[],2:[],3:[],4:[]}
direction=[0 for _ in range(12)]
totalSize=1
holeSize=1

for i in range(6):
    a,b=map(int,sys.stdin.readline().split())
    farm[a].append(b)
    direction[i]=a
    direction[i+6]=a


for i in range(1,5):
    if len(farm[i])==1:
        totalSize=totalSize*farm[i][0]

for i in range(3, 12):
    if direction[i-3]==direction[i-1] and direction[i-2]==direction[i]:
        if i<6:
            holeSize=farm[direction[i-1]][1]*farm[direction[i]][0]
            break
        elif i==6:
            holeSize = farm[direction[i - 1]][1] * farm[direction[i]][1]
            break
        elif i==8:
            holeSize = farm[direction[i - 1]][0] * farm[direction[i]][0]
        else:
            holeSize = farm[direction[i - 1]][0] * farm[direction[i]][1]
            break


print((totalSize-holeSize)*fruit)