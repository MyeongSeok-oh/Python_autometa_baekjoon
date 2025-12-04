'''
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 모음(a, e, i, o, u)의 개수를 출력하는 프로그램을 작성하시오.
'''

word = input()

count = 0 
for i in word:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count += 1

print(count)