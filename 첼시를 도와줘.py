'''
첫 번째 줄에는 테스트 케이스의 개수 n이 주어진다 (n≤100). 

각 테스트 케이스의 첫 번째 줄 p는 고려해야될 선수의 수이다 (1≤p≤100).  

그 아래 p개의 줄에는 선수의 정보가 표시된다. 

각각의 줄은 선수의 가격 C 와 이름을 입력한다 (C<2*109).

각각의 테스트 케이스에서 가장 비싼 선수의 이름을 출력해야한다.
'''

n = int(input())

max_C = 0
max_player = ""

for _ in range(n):
    p = int(input())
    for _ in range(p):
        C, player = input().split()
        C = int(C)

        if C > max_C:
            max_C = C
            max_player = player

    print(max_player)
    max_C = 0
    max_player = ""