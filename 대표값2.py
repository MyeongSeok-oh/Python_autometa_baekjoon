'''
다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.
'''
nums = [int(input()) for _ in range(5)]
nums.sort()

print(sum(nums)//5)
print(nums[2])