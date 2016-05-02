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

def key(pair):
    return ",".join((str(pair[0]),str(pair[1])))

greatest_size = 0
for i, row in enumerate(A):
    for j, val in enumerate(row):
        if not val:
            continue
        neighbours = [(i-1,j), (i, j-1), (i-1, j-1), (i-1, j+1)]
        total_size = 1
        cur_head = {
            "head": key((i,j)),
            "size": 0
        }

        for dot in neighbours:
            if not key(dot) in head:
                continue
            island = head[key(dot)]
            if island["head"] == cur_head["head"]:
                continue
            total_size += island["size"]
            if island["size"] >= cur_head["size"]:
                cur_head = {
                    "head": island["head"],
                    "size": island["size"]
                }

        cur_head['size'] = total_size
        if total_size > greatest_size:
            greatest_size = total_size
        # import pdb; pdb.set_trace()
        head[key((i,j))] = cur_head
        for dot in neighbours:
            if not key(dot) in head:
                continue
            head[key(dot)] = cur_head

print 'A: %s' % A
print greatest_size
for key, val in head.iteritems():
    print 'Heads: %s ---  %s ' % (key, val)
