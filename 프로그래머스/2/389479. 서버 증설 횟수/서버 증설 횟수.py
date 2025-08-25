def solution(players, m, k):
    answer = 0
    time=[0 for _ in range(24)]
    for i in range(24):
        if players[i]>=m:
            if players[i]<(time[i]+1)*m:
                continue
            else:
                server_c = players[i]//m
                add_server = server_c - time[i]
                for j in range(i,i+k):
                    if j>23:
                        break;
                    time[j]=time[j]+add_server
        else:
            continue

        answer = answer + add_server

    return answer