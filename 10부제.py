'''
날짜의 일의 자리 숫자가 주어지고 5대의 자동차 번호의 일의 자리 숫자가 주어졌을 때 위반하는 자동차의 대수를 출력하면 된다. 
'''

day = int(input())
cars = list(map(int, input().split()))

print(cars.count(day))