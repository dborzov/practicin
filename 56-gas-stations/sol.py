class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if len(gas)==0:
            return -1
        def res(i):
            i = i % len(gas)
            return gas[i] - cost[i]

        cur = 0

        max_streak_val = 0
        max_streak_start = 0
        max_streak_end = 0

        cur_streak_start = 0
        cur_streak_val = 0
        for i in range(2*len(gas)):
            cur += res(i)
            if cur_streak_val <= 0:
                cur_streak_start = i
                cur_streak_val = 0
            cur_streak_val += res(i)
            if cur_streak_val > max_streak_val:
                max_streak_start = cur_streak_start
                max_streak_val = cur_streak_val
                max_streak_end = i
        if cur <0:
            return -1
        return max_streak_start % len(gas)
