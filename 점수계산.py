'''
Docstring for Python배우기_autometa_baekjoon.점수계산
'''

N = int(input())

score = 0
total = 0

nums = list(map(int, input().split()))
for i in nums:
    if i == 1:
        score += 1
        total += score
    if i == 0:
        score = 0

print(total)