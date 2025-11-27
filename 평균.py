'''
세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 

그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.
'''

N = int(input())

scores = list(map(int, input().split()))
M = max(scores)

new_scores = []
for num in scores:
    num = (num/M) * 100
    new_scores.append(num)

print(sum(new_scores)/len(new_scores))