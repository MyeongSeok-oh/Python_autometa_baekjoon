'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
'''
import math

N = int(input())
count = 0
nums = list(map(int, input().split()))

for num in nums:
    if num < 2:  # 1은 소수 아님
        continue
    
    is_prime = True
    for j in range(2, int(math.sqrt(num)) + 1):
        if num % j == 0:  # 나누어떨어지면
            is_prime = False  # 소수 아님
            break
    
    if is_prime:
        count += 1

print(count)