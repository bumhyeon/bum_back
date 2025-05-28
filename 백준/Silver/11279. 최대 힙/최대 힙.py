import heapq
import sys

input = sys.stdin.readline  # input을 sys.stdin.readline으로 대체
num = int(input())
node = []
sell = []

for _ in range(num):
    water = int(input())
    if water > 0:
        heapq.heappush(node, -water)  # 최대 힙처럼 사용하기 위해 음수로 저장
    elif water == 0:
        if node:
            a = -heapq.heappop(node)  # 가장 큰 값을 꺼내서 양수로 변환
            sell.append(a)            # 양수로 변환된 값을 sell에 추가
        else:
            sell.append(0)            # node가 비어 있을 때 0 추가

# 최종 결과를 한 번에 출력
sys.stdout.write('\n'.join(map(str, sell)) + '\n')
