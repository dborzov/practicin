A = [9,4,7,2,19,3,12, 3, 17, 9, 23, 7, 52]
B = [7, 3, 9]

def find_sublist(universe, uniques):
    recents =  {val: False for val in uniques}
    ll_order = {val:(None, None) for val in uniques}
    head, tail = None, None
    count_identified = 0
    cur_leftmost = 0
    lowest_length = len(universe)
    for i, item in enumerate(universe):
        if not(item in recents):
            continue
        if recents[item] is False:
            count_identified += 1
            if head is None:
                head = item
        else:

        recents[item]= i
        if not count_identified==len(uniques):
            continue
        cur_length = i - recents[head]
        if cur_length < lowest_length:
            print 'reassigning to: {}->{}'.format(i,recents[head])
            lowest_length = cur_length
    return lowest_length if count_identified==len(uniques) else None

print find_sublist(A, B)
