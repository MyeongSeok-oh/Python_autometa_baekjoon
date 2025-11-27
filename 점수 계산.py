'''
Docstring for Python배우기_autometa_baekjoon.점수 계산
'''
scores = []

for i in range(1, 9):
    score = int(input())
    scores.append((score, i))

scores.sort(reverse=True)

top5 = scores[:5]

total = sum(s[0] for s in top5)

problems = sorted([s[1] for s in top5])

print(total)
print(*problems)