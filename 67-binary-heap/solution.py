class Heap:
    def __init__(self):
       self.bh = []

    def pop(self):
       if len(self.bh)==0: raise StandardError('No more elements in the heap')
       if len(self.bh)==1:
        	return self.bh.pop()
       return_value, self.bh[0] = self.bh[0],  self.bh[-1]
       self.bh = self.bh[:len(self.bh)-1]
       cur = 0
       while True:
        left, right = cur*2+1, cur*2+2
        get_value = lambda x:self.bh[x] if x<len(self.bh) else None
        top_element = max([left, right], key=get_value)
        print "Stack:", self.bh
        print "Left:{}, right:{}, top element:{}".format(left, right, top_element)
        if (get_value(top_element) is None) or (self.bh[top_element] < self.bh[cur]):
        	return return_value
        self.bh[cur], self.bh[top_element] = self.bh[top_element], self.bh[cur]
        cur = top_element


    def bubble_up(self,cur):
      	while cur!=0:
    		parent=(cur-1)//2
    		if self.bh[parent]>self.bh[cur]:
    			return
    		self.bh[parent], self.bh[cur] = self.bh[cur], self.bh[parent]
    		cur=parent

    def add(self, new_value):
    	self.bh.append(new_value)
      	self.bubble_up(len(self.bh)-1)
        print 'We added {}, and now stack is {}'.format(new_value, self.bh)


new_one = Heap()
new_one.add(3)
new_one.add(2)
new_one.add(12)
new_one.add(9)
print 'Pop: ', new_one.pop()
print 'Pop: ', new_one.pop()
print 'Pop: ', new_one.pop()
