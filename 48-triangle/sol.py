class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==0:
            return 0
        shortest_sum = [[triangle[0][0]]]
        for level in triangle[1:]:
            shortest_sum.append([])
            for i, element in enumerate(level):
                shortest_case = min([shortest_sum[-2][idx] for idx in [i-1, i] if idx >=0 and idx<len(level)-2])
                shortest_sum[-1].append(shortest_case + element)
        return min(shortest_sum[-1])
