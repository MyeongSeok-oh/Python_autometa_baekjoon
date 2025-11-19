'''
서로 다른 N개의 자연수의 합이 S라고 한다. 

S를 알 때, 자연수 N의 최댓값은 얼마일까?
'''

S = int(input())

N = 0
total = 0

while  total + N + 1 <= S:
    N += 1
    total += N

print(N)