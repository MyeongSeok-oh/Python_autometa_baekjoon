'''
아홉 난쟁이의 모자에 쓰여 있는 수가 주어졌을 때, 일곱 난쟁이를 찾는 프로그램을 작성하시오. (아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾으시오)
'''

nums = [int(input()) for _ in range(9)]
fake_sum = sum(nums) - 100

for i in range(9):
    for j in range(i+1, 9):
        if nums[i] + nums[j] == fake_sum:
            fake1, fake2 = nums[i], nums[j]
            break
        else:
            continue
        break

nums.remove(fake1)
nums.remove(fake2)

nums.sort()
for i in range(7):
    print(nums[i])