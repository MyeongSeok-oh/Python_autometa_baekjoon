'''
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
'''

N, K = map(int, input().split())

nums = []
for i in range(1, N+1):
    if N % i == 0:
        nums.append(i)

if len(nums) < K:
    print(0)
else:
    print(nums[K-1])