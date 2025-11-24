'''
입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.

각 테스트 케이스는 9줄에 걸쳐서 입력되며, 매 줄마다 해당 회의 연세대 득점 Y와 고려대 득점 K가 공백으로 구분되어 주어진다. 이 두 수는 0이상 9이하이다.

각각의 케이스마다 한 줄에 연세대가 이겼을 경우 "Yonsei", 고려대가 이겼을 경우 "Korea", 비겼을 경우 "Draw"를 출력한다.
'''

T = int(input())

Y_score = 0
K_score = 0

for _ in range(T):
    for _ in range(9):
        Y, K = map(int, input().split())
        Y_score += Y
        K_score += K

    if Y_score > K_score:
        print("Yonsei")
    elif Y_score < K_score:
        print("Korea")
    else:
        print("Draw")