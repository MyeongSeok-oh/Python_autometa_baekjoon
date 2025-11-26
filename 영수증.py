'''
책 10권의 총 가격과 가격을 읽을 수 있는 9권 가격이 주어졌을 때, 가격을 읽을 수 없는 책의 가격을 구하는 프로그램을 작성하시오.
'''

total = int(input())
price = 0
for i in range(9):
    n = int(input())
    price += n

print(total - price)
