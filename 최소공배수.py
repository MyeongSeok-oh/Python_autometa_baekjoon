'''
두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
'''

import math

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    lcm = (A * B) // math.gcd(A, B)
    print(lcm)

'''
[유클리드 호제법] _ GCD(최대공약수) 구하기
~~ 파이썬에서는 math 라이브러리로 해결 가능! ~~
a, b = A, B
    while b != 0:
        a, b = b, a % b
    gcd = a
'''