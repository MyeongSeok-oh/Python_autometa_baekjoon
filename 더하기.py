'''
10보다 작거나 같은 자연수 N개를 주면 합을 구하는 프로그램을 작성하시오.
'''

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    print(sum(nums))
