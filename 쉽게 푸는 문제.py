'''
1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

첫째 줄에 구간의 시작과 끝을 나타내는 정수 A, B(1 ≤ A ≤ B ≤ 1,000)가 주어진다. 

즉, 수열에서 A번째 숫자부터 B번째 숫자까지 합을 구하면 된다.
'''
A, B = map(int, input().split())

nums = []
num = 1

while len(nums) < B:
    nums.extend([num]*num)
    num += 1

print(sum(nums[A-1:B]))
