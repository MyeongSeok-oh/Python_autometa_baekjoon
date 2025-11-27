'''
Docstring for Python배우기_autometa_baekjoon.오타맨 고창영
'''
T = int(input())

for _ in range(T):
    A, B = input().split()
    A = int(A)

    print(B[:A-1]+B[A:])