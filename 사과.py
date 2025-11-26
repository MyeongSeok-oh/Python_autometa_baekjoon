'''
각 학교의 학생 수와 사과 개수가 주어졌을 때, 학생들에게 나눠주고 남는 사과의 총 개수를 구하는 프로그램을 작성하시오.
'''

N = int(input())
remain = 0

for _ in range(N):
    student, apple = map(int, input().split())
    remain += (apple%student)

print(remain)