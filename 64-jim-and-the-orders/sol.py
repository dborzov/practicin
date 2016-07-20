import heapq
import sys

queue = []
n = int(raw_input())
for i in range(1,n+1):
        f = sum([int(e) for e in raw_input().split(" ")])
        # print " %d==> %d" % (i,f)
        heapq.heappush(queue, (f*10000+i,i) )

for j in range(n):
    sys.stdout.write(str(heapq.heappop(queue)[1]))
    if j==n-1:
        break
    sys.stdout.write(" ")
sys.stdout.write("\n")
