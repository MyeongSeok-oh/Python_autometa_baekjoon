'''
긴 형태의 알고리즘 이름이 주어졌을 때, 이를 짧은 형태로 바꾸어 출력하는 프로그램을 작성하시오.
'''
names = list(input().split("-"))

short_names = []
for name in names:
    short_names.append(name[0])

print(''.join(short_names))
