def solution(mats, park):
    answer = -1
    height = len(park);
    width = len(park[0]);
    mats.sort()
    smallest = mats[0]
    for i in range(0, height - smallest + 1):
        for j in range(0, width - smallest + 1):
            if park[i][j] == '-1':
                answer = unfold(i, j, park, mats, answer)

    print(answer)

    return answer


def unfold(y, x, park, mats, answer):
    for size in mats:
        if x + size > len(park[0]) or y + size > len(park):
            continue
        for i in range(y, y + size):
            for j in range(x, x + size):
                if park[i][j] != '-1':
                    return answer
        if size > answer:
            answer = size


    return answer
