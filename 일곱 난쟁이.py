'''

'''
nums = [int(input()) for _ in range(9)]

total = sum(nums)
fake_sum = total - 100

for i in range(9):
    for j in range(i+1, 9):
        if nums[i] + nums[j] == fake_sum:
            fake1, fake2 = nums[i], nums[j]
            nums.remove(fake1)
            nums.remove(fake2)
            break
    else:
        continue
    break

nums.sort()
for i in range(7):
    print(nums[i])