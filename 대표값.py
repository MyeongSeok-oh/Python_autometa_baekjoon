'''
첫째 줄부터 열 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 

주어지는 자연수는 1,000 보다 작은 10의 배수이다.

첫째 줄에는 평균을 출력하고, 둘째 줄에는 최빈값을 출력한다. 

최빈값이 둘 이상일 경우 그 중 하나만 출력한다. 

평균과 최빈값은 모두 자연수이다.
'''

nums = []
count = 0
for _ in range(10):
    nums.append(int(input()))
    
print(sum(nums)//10)

from collections import Counter
counter = Counter(nums)
print(counter.most_common(1)[0][0])