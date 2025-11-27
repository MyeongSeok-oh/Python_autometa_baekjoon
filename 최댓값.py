'''
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
'''
count = 0
max_num = 0
max_count = 0

for _ in range(9):
    num = int(input())
    count += 1
    if num > max_num:
        max_num = num
        max_count = count

print(max_num)
print(max_count)


# # [리스트를 이용해서 풀기]
# numbers = []
# for _ in range(9):
#     numbers.append(int(input()))

# max_value = max(numbers)
# max_index = numbers.index(max_value) + 1  # 1번째부터 시작

# print(max_value)
# print(max_index)
