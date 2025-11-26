'''
하나의 콘센트가 있고, N개의 멀티탭이 있다. 각 멀티탭은 몇 개의 콘센트로 이루어져 있다고 한다. 

최대 몇 대의 컴퓨터를 전원에 연결할 수 있을까?
'''

N = int(input())
total = 0

for _ in range(N):
    num = int(input())
    total += (num-1)

print(total+1)