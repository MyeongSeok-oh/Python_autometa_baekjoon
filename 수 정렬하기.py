'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
N = int(input())

nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)
    nums.sort()

for i in range(len(nums)):
    print(nums[i])