import thread, time

shared = []


def spammer(prefix, hasher):
    i = 0
    while i<10000000:
        i += 1
        label = prefix + str(i)
        hasher[label] = True
        shared.append(label)
    print 'finished: ', prefix

thread1, thread2 = {}, {}

thread.start_new_thread( spammer, ("Misha", thread1))
thread.start_new_thread( spammer, ("Lisa", thread2))

time.sleep(10)
print '---- now starting to check stuff'
for each in shared:
    if each in thread1:
        continue
    if each in thread2:
        continue
    print 'a missed item: ', each

import pdb; pdb.set_trace()
