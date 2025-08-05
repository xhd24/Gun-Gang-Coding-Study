def solution(schedules, timelogs, startday):
    answer = 0
    weekend = 7 - startday;
    for timelog in timelogs:
        del timelog[weekend]
        del timelog[weekend - 1]
    idx = 0

    for i in range(0, len(schedules)):
        schedules[i] += 10
        if schedules[i] % 100 >= 60:
            schedules[i] += 40

    print(schedules)
    for timelog in timelogs:
        absent = False
        for time in timelog:
            if time > schedules[idx]:
                absent = True
                break
        idx += 1
        if absent == False:
            answer += 1

    return answer
