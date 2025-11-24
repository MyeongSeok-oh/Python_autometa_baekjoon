'''
M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오. 

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 64, 81, 100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.
'''

M = int(input())
N = int(input())

squares = []
i = 1

while i*i <= N:
    if i*i >= M:
        squares.append(i*i)
    i += 1

if squares:
    print(sum(squares))
    print(squares[0])
else:
    print(-1)