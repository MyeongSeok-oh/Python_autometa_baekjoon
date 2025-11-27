'''
양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오.
'''

T = int(input())
point = []

for _ in range(T):
    n = int(input())
    nums = bin(n)[2:]

    for i in range(len(nums)-1, -1, -1):
        if nums[i] == "1":
            point.append(len(nums)-1-i)

print(*point)