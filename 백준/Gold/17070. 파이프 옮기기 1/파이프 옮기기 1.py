import sys
from collections import deque

size=int(sys.stdin.readline())
house=[0 for _ in range(size)]
queue=deque()
count=0

def parse(this_row, this_column, this_form):
    if this_row == size-1 and this_column == size-1:
        global count
        count+=1
        return 0
    if this_row>=size or this_column>=size:
        return 0

    if this_form==0:
        if this_column+1<=size-1 and house[this_row][this_column + 1] == 0:
            parse(this_row, this_column + 1, 0)
        if this_column+1<=size-1 and this_row+1<=size-1 and house[this_row][this_column + 1] == 0 and house[this_row + 1][this_column + 1] == 0 and house[this_row + 1][this_column] == 0:
            parse(this_row + 1, this_column + 1, 1)
    elif this_form==1:
        if this_column+1<=size-1 and house[this_row][this_column+1] == 0:
            parse(this_row,this_column+1,0)
        if this_column+1<=size-1 and this_row+1<=size-1 and house[this_row][this_column+1]==0 and house[this_row+1][this_column+1]==0 and house[this_row + 1][this_column] == 0:
            parse(this_row+1,this_column+1,1)
        if this_row+1<=size-1 and house[this_row+1][this_column]==0:
            parse(this_row+1,this_column,2)
    else:
        if this_row+1<=size-1 and house[this_row+1][this_column] == 0:
            parse(this_row+1, this_column, 2)
        if this_column+1<=size-1 and this_row+1<=size-1 and house[this_row][this_column + 1] == 0 and house[this_row + 1][this_column + 1] == 0 and house[this_row + 1][
            this_column] == 0:
            parse(this_row + 1, this_column + 1, 1)

for i in range(size):
    house[i]=list(map(int,sys.stdin.readline().split()))

form=0 #0은 가로 1은 대각선 2는 세로
place=(0,1,0)

if house[place[0]][place[1]+1] == 0:
    queue.append((place[0],place[1]+1,0))
if house[place[0]+1][place[1]+1] == 0 and house[place[0]][place[1]+1] == 0 and house[place[0]+1][place[1]] == 0:
    queue.append((place[0]+1,place[1]+1,1))

while queue:
    place_row,place_column,place_form=queue.popleft()
    parse(place_row, place_column, place_form)

print(count)
