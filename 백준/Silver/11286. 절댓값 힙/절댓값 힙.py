import heapq
import sys

input = sys.stdin.readline
palm = []
pay = int(input())

for i in range(pay):
    coconut = int(input())
    if coconut != 0:
        # 절댓값 기준으로 힙에 추가하기 위해 (절댓값, 실제 값) 형태로 저장
        heapq.heappush(palm, (abs(coconut), coconut))
    elif coconut == 0:
        if palm:
            # 절댓값이 가장 작은 값 꺼내기, 두 번째 요소로 실제 값을 꺼냄
            i, a = heapq.heappop(palm)
            print(a)
        else:
            print(0)  # 힙이 비어 있을 때 0 출력
