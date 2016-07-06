class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        while True:
            if nums[idx-1] < nums[idx]:
                idx = idx-1
            else:
                return nums[idx]
