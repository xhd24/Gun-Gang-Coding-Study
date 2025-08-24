def solution(m, n, board):
    _board = []
    answer = 0
    flag=True

    for v in board:
        _board.append(list(v))

    while(flag):
        queue = []

        for i in range(m - 1):
            for j in range(n - 1):
                block1 = _board[i][j]
                block2 = _board[i][j + 1]
                block3 = _board[i + 1][j]
                block4 = _board[i + 1][j + 1]
                if block1 == block2 == block3 == block4 and block1 != 0:
                    queue.append((i, j))
                    queue.append((i, j + 1))
                    queue.append((i + 1, j))
                    queue.append((i + 1, j + 1))
                else:
                    continue
        if (len(queue) == 0):
            flag=False
            break

        queue2 = set(queue)
        queue3 = sorted(list(queue2), key=lambda x: x[0])

        while (queue3):
            i, j = queue3.pop(0)
            answer = answer + 1
            fall(i, j, _board)

    return answer

def fall(i,j,_board):
    if i==0:
        _board[i][j]=0
        return _board
    _board[i][j]=_board[i-1][j]
    fall(i-1,j,_board)
    return _board
