'''
Docstring for Python배우기_autometa_baekjoon.숫자의 개수
'''
A = int(input())
B = int(input())
C = int(input())

N = str(A * B * C)

zero_count = 0
one_count = 0
two_count = 0
three_count = 0
four_count = 0
five_count = 0
six_count = 0
seven_count = 0
eight_count = 0
nine_count = 0

for num in N:
    if num == "0":
        zero_count += 1
    elif num == "1":
        one_count += 1
    elif num == "2":
        two_count += 1
    elif num == "3":
        three_count += 1
    elif num == "4":
        four_count += 1
    elif num == "5":
        five_count += 1
    elif num == "6":
        six_count += 1
    elif num == "7":
        seven_count += 1
    elif num == "8":
        eight_count += 1
    else:
        nine_count += 1

print(zero_count)
print(one_count)
print(two_count)
print(three_count)
print(four_count)
print(five_count)
print(six_count)
print(seven_count)
print(eight_count)
print(nine_count)


# # 간단하게 출력하기
# A = int(input())
# B = int(input())
# C = int(input())

# result = str(A * B * C)

# for i in range(10):
#     print(result.count(str(i)))