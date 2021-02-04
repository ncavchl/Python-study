# import datetime 

def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    weekday = ["FRI", "SAT","SUN","MON","TUE", "WED", "THU"]
    answer = weekday[(sum(month[:a-1])+b-1)%7]
    # day = datetime.datetime(2016, a, b)
    # #print(day.weekday())
    # dt = day.weekday()
    # answer = weekday[dt]
    return answer