'''
input : 1
*

input : 2
* *
 * *

input : 3
* * *
 * * *
* * *

예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
'''
N = int(input())

for i in range(N):
    if i % 2 == 0:
        print("* "*N)
    else:
        print(" "+"* "*N)