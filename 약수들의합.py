'''
어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.

n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)

입력의 마지막엔 -1이 주어진다.
'''

while True:
    num = int(input())

    if num == -1:
        break

    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)

    if sum(divisors) == num:
        result = " + ".join(map(str, divisors))
        print(f"{num} = {result}")
    else:
        print(f"{num} is NOT perfect.")