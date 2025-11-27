'''
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
'''
import math

M = int(input())
N = int(input())

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

primes = []
for num in range(M, N+1):
    if is_prime(num):
        primes.append(num)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)