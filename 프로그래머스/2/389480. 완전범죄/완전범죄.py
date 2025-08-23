def solution(info, n, m):
    INF = float('inf')

    answer = 0

    dp = [[INF] * m for _ in range(len(info) + 1)]
    dp[0][0] = 0

    for i in range(0, len(info)):
        a_val, b_val = info[i]
        for b in range(m):
            if dp[i][b] == INF:
                continue

            # a가 훔친 경우
            if dp[i][b] + a_val < n:
                dp[i + 1][b] = min(dp[i + 1][b], dp[i][b] + a_val)

            # b가 훔친 경우
            if b + b_val < m:
                dp[i + 1][b + b_val] = min(dp[i + 1][b + b_val], dp[i][b])

    answer = min(dp[len(info)])
    if answer == INF:
        answer = -1

    return answer