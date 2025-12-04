'''
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 

이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
'''
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0
for i in range(N-1, -1, -1):
    if K >= coins[i]:
        count += (K // coins[i])
        K %= coins[i]

print(count)