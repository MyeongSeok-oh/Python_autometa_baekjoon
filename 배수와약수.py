'''
입력은 여러 테스트 케이스로 이루어져 있다. 

각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.
'''

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    elif A % B == 0:
        print("multiple")
    elif B % A == 0:
        print("factor")
    else:
        print("neither")