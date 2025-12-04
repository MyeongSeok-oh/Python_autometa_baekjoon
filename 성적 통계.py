'''
중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.
'''
K = int(input())

for i in range(1, K+1):
    data = list(map(int, input().split()))
    N = data[0]
    scores = data[1:]

    scores.sort(reverse=True)

    max_gap = 0
    for j in range(len(scores)-1):
        gap = scores[j] - scores[j+1]
        max_gap = max(max_gap, gap)
    
    print(f"Class {i}")
    print(f"Max {max(scores)}. Min {min(scores)}, Largest gap {max_gap}")