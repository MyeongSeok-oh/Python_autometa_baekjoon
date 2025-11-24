'''
어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.
'''

n = int(input())

youngest_name = ""
youngest_birth = (0, 0, 0)  # (년, 월, 일)

oldest_name = ""
oldest_birth = (9999, 12, 31)  # 큰 값으로 초기화

for _ in range(n):
    data = input().split()
    name = data[0]
    dd = int(data[1])
    mm = int(data[2])
    yyyy = int(data[3])
    birth = (yyyy, mm, dd)
    
    # 나이가 적다 = 생일이 더 최근
    if birth > youngest_birth:
        youngest_birth = birth
        youngest_name = name
    
    # 나이가 많다 = 생일이 더 오래됨
    if birth < oldest_birth:
        oldest_birth = birth
        oldest_name = name

print(youngest_name)
print(oldest_name)