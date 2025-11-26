'''
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
'''

n = int(input())

F = [0, 1]
for i in range(n+1):
    F.append(F[i]+F[i+1])

print(F[n])

'''
[다른 해결법]
n = int(input())

a, b = 0, 1
for _ in range(n):
    a, b = b, a + b  # 동시 할당으로 다음 피보나치 수 계산

print(a)
'''