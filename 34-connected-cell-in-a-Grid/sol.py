import sys


input = open(sys.argv[1], 'rb')
def readline():
    return input.readline().rstrip()

M = int(readline())
N= int(readline())


A = []
for _ in range(M):
    line = readline().split(' ')
    cur_row = [True if sym=='1' else False for sym in line]
    A.append(cur_row)

head = {}
island_sizes = {}


def key(pair):
    return ",".join((str(pair[0]),str(pair[1])))

def get_head(pair):
    cur = pair
    while cur != head[cur]:
        cur = head[cur]
    return cur

def union(a,b):
    head_a = get_head(a)
    head_b = get_head(b)
    if head_a == head_b:
        return head_a
    if island_sizes[head_a] >= island_sizes[head_b]:
        eaten = head_a
        eater = head_b
    else:
        eaten = head_b
        eater = head_a
    island_sizes[eater] += island_sizes[eaten]
    head[a] = eater
    head[b] = eater
    head[head_a] = eater
    head[head_b] = eater
    del island_sizes[eaten]
    return eater




for i, row in enumerate(A):
    for j, val in enumerate(row):
        if not val:
            continue
        neighbours = [(i-1,j), (i, j-1), (i-1, j-1), (i-1, j+1)]
        cur = key((i,j))
        head[cur] = cur
        island_sizes[cur] = 1

        for dot in neighbours:
            if not key(dot) in head:
                continue
            cur = union(cur, key(dot))
            if not cur:
                import pdb; pdb.set_trace()


# print 'A: %s' % A
print max(island_sizes.values())
