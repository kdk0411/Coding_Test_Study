import datetime as dt
def solution(a, b):
    weekday_dict = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    ret = dt.datetime(2016, a, b)
    sr = weekday_dict[ret.weekday()]
    return sr