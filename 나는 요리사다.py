'''
총 다섯 개 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 구분되어 주어진다. 

첫 번째 참가자부터 다섯 번째 참가자까지 순서대로 주어진다. 

항상 우승자가 유일한 경우만 입력으로 주어진다.

첫째 줄에 우승자의 번호와 그가 얻은 점수를 출력한다.
'''
max_score = 0
winner = 0

for i in range(1, 6):
    scores = list(map(int, input().split()))
    total = sum(scores)

    if total > max_score:
        max_score = total
        winner = i

print(winner, max_score)