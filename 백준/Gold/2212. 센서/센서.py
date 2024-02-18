import sys

sensorN=int(input())
centerN=int(input())
sensorList=list(map(int,input().split()))
distanceList=[0 for _ in range(sensorN)]
answer=0
sensorList.sort()


for i in range(sensorN-1):
    distanceList[i]=sensorList[i+1]-sensorList[i]

for i in range(centerN-1):
    max_dist=distanceList.index(max(distanceList))
    distanceList[max_dist]=0

for i in distanceList:
    answer+=i

print(answer)