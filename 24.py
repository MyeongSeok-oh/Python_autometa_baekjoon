'''
도현이는 선영이를 임무를 시작한지 정확하게 24시간이 되는 순간에 잡으려고 한다.

만약 지금 시간이 13:52:30이고, 임무를 시작한 시간이 14:00:00 이라면 도현이에게 남은시간은 00:07:30 이다.

모든 시간은 00:00:00 ~ 23:59:59로 표현할 수 있다. 입력과 출력에 주어지는 모든 시간은 XX:XX:XX 형태이며, 숫자가 2자리가 아닐 경우에는 0으로 채운다.

도현이가 임무를 시작한 시간과, 현재 시간이 주어졌을 때, 도현이에게 남은 시간을 구하는 프로그램을 작성하시오.
'''

current = input().split(":")
start = input().split(":")

current_time = int(current[0])*3600 + int(current[1])*60 + int(current[2])
start_time = int(start[0])*3600 + int(start[1])*60 + int(start[2])

remain = (start_time + 24*3600) - current_time

if remain >= 24*3600:
    remain -= 24*3600

hour = remain // 3600
minute = (remain%3600) // 60
sec = remain % 60

print(f"{hour:02d}:{minute:02d}:{sec:02d}")