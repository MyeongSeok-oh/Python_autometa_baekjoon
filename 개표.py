'''
A와 B가 한 오디션 프로의 결승전에 진출했다. 

결승전의 승자는 심사위원의 투표로 결정된다.

심사위원의 투표 결과가 주어졌을 때, 어떤 사람이 우승하는지 구하는 프로그램을 작성하시오.
'''

V = int(input())
vote = input()

count_A = 0
count_B = 0

for i in range(V):
    if vote[i] == "A":
        count_A += 1
    else:
        count_B += 1

if count_A > count_B:
    print("A")
elif count_A < count_B:
    print("B")
else:
    print("Tie")

'''
[count() 메서드 사용]
V = int(input())
vote = input()

count_A = vote.count("A")
count_B = vote.count("B")

if count_A > count_B:
    print("A")
elif count_A < count_B:
    print("B")
else:
    print("Tie")
'''