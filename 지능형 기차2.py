'''
10개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 

기차에 사람이 가장 많을 때의 사람 수를 계산하는 프로그램을 작성하시오.
'''
num = 0
max_num = 0

for _ in range(10):
    OUT, IN = map(int, input().split())
    num += (IN - OUT)
    max_num = max(max_num, num)

print(max_num)