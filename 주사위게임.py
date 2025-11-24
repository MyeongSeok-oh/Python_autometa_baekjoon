'''
게임을 시작하는 시점에서, 두 사람의 점수는 모두 100점이다.

게임은 여섯 면 주사위를 사용하며, 라운드로 진행된다. 매 라운드마다, 각 사람은 주사위를 던진다. 낮은 숫자가 나온 사람은 상대편 주사위에 나온 숫자만큼 점수를 잃게 된다. 두 사람의 주사위가 같은 숫자가 나온 경우에는 아무도 점수를 잃지 않는다.

게임이 끝난 이후에 두 사람의 점수를 구하는 프로그램을 작성하시오.
'''

n = int(input())

A_score = 100
B_score = 100

for _ in range(n):
    A, B = map(int, input().split())

    if A > B:
        B_score -= A
    elif A < B:
        A_score -= B

print(A_score)
print(B_score)
