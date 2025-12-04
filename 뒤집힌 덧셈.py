'''
Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자.

두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오
'''
X, Y = input().split()

X = int(X[::-1])
Y = int(Y[::-1])

print(int(str(X+Y)[::-1]))