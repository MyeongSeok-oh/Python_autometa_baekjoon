'''
이번이 두 대학에서 모두 10 명씩이 콘테스트에 참여했다. 

긴 논의 끝에 참가한 10 명 중 득점이 높은 사람에서 3 명의 점수를 합산하여 대학의 득점으로하기로 했다.

W 대학 및 K 대학 참가자의 점수 데이터가 주어진다. 

이때, 각각의 대학의 점수를 계산하는 프로그램을 작성하라.
'''
W_scores = [int(input()) for _ in range(10)]
K_scores = [int(input()) for _ in range(10)]

W_scores.sort(reverse=True)
K_scores.sort(reverse=True)

print(sum(W_scores[0:3]))
print(sum(K_scores[0:3]))