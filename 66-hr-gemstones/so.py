N = int(raw_input())
prev = {}
for el in raw_input().strip():
    prev[el] = True

for _ in range(N-1):
    cur = {}
    for el in raw_input().strip():
        if el in prev:
            cur[el] = True
    prev = cur

print len(prev.keys())
