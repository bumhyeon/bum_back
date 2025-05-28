import sys
import heapq

hip = []
input = sys.stdin.readline
num = int(input())
i = 0

while i < num:
    i += 1
    n = int(input())
    if  n > 0 :
        heapq.heappush(hip,n)
    elif n==0 :
        if hip:
            print(heapq.heappop(hip))    
        else:
            print(0)