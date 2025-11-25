'''
두 세자리 수 입력.

세자리 수를 거꾸로 입력 받은 후, 더 큰 수를 출력한다.
'''

A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])

print(max(A, B))