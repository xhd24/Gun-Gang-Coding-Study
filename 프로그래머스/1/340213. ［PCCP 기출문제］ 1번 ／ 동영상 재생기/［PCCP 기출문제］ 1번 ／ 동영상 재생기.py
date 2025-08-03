def solution(video_len, pos, op_start, op_end, commands):

    video_time = to_time(video_len)
    pos_time = to_time(pos)
    op_Stime = to_time(op_start)
    op_Etime = to_time(op_end)

    for i in commands:
        #오프닝 구간이면 건너뛰기
        if pos_time<=op_Etime and pos_time>=op_Stime:
            pos_time = op_Etime

        if i == "next":
            # 10초 건너뛰기, 남은 시간이 10초보다 짧으면 마지막으로
            pos_time = video_time if pos_time+10>video_time else pos_time+10
            if pos_time <= op_Etime and pos_time >= op_Stime:
                pos_time = op_Etime
        elif i == "prev":
        #10초 전으로, 10초 보다 덜 갔으면 처음으로
            pos_time = 0 if pos_time-10<0 else pos_time-10
            if pos_time<=op_Etime and pos_time>=op_Stime:
                pos_time = op_Etime

    answer = "{:02d}:{:02d}".format(int(pos_time/60),pos_time%60)
    return answer

def to_time(str):
    min, sec = map(int,str.split(":"))
    time = 60*min+sec
    return time