def solution(video_len, pos, op_start, op_end, commands):
    answer = ""

    v = makeTimeToSecond(video_len)
    p = makeTimeToSecond(pos)
    s = makeTimeToSecond(op_start)
    e = makeTimeToSecond(op_end)

    p = curPos(v, p, s, e)

    for c in commands:
        p = curPos(v, p-10 if c == "prev" else p+10, s, e)

    p = curPos(v, p, s, e)

    min = p // 60
    sec = p % 60

    return makeTimeToString(min) + ":" + makeTimeToString(sec)

def curPos(v_int, p_int, s_int, e_int):
    if p_int <= 0:
        p_int = 0
    if s_int <= p_int <= e_int:
        return e_int
    if v_int <= p_int:
        return v_int
    return p_int

def makeTimeToString(time):
    if len(str(time)) == 0:
        return "00"
    if len(str(time)) == 1:
        return "0"+str(time)
    return str(time)

def makeTimeToSecond(time):
    t = time.split(":")
    return int(t[0])*60 + int(t[1])
