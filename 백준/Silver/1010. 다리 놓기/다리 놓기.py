import sys

repeat=int(sys.stdin.readline())

for i in range(repeat):
    west, east = map(int, sys.stdin.readline().split())
    case=1
    for j in range(east,east-west,-1):
        case*=j
    for j in range(west,1,-1):
        case=case//j
    print(case)
