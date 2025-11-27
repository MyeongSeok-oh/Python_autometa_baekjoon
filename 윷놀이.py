''' 
네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중 어떤 것인지를 결정하는 프로그램을 작성하라.
'''


for _ in range(3):
    nums = list(map(int, input().split()))

    count = 0
    for i in nums:
        if i == 0:
            count += 1

    if count == 0:
        print("E")
    elif count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    elif count == 4:
        print("D")
