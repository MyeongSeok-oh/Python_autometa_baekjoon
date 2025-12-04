'''
문장을 읽은 뒤, 줄의 첫 글자를 대문자로 바꾸는 프로그램을 작성하시오.
'''
N = int(input())

for _ in range(N):
    sentence = list(input().split())
    sentence[0] = sentence[0].title()
    print(' '.join(sentence))
    