'''
4개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 프로그램을 작성하시오.
'''
count = 0
max_count = count

for _ in range(4):
    OUT, IN = map(int, input().split())
    count = count + IN - OUT
    if max_count < count:
        max_count = count

print(max_count)