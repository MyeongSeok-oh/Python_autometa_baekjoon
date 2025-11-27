'''
정수 세 개가 주어진다. 

제일 작은 수, 그 다음 수, 제일 큰 수를 차례대로 출력한다.
'''
nums = list(map(int, input().split()))
nums.sort()
print(*nums)