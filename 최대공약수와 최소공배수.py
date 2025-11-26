'''
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
'''
import math

A, B = map(int, input().split())

print(math.gcd(A, B))
print((A*B) // math.gcd(A, B))