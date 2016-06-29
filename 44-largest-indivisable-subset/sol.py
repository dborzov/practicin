class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        nums = sorted(nums)
        refs = [i for i in range(len(nums))]
        tall = [1 for i in range(len(nums))]
        tallest_so_far = 0
        for i in range(len(nums)):
            j= i-1
            dividers = []
            while j>=0:
                if nums[i] % nums[j] == 0:
                    dividers.append(j)
                j = j-1
            if len(dividers)==0:
                continue
            tallest_idx = dividers[0]
            for div_idx in dividers:
                if tall[div_idx] > tall[tallest_idx]:
                    tallest_idx = div_idx
            refs[i] = tallest_idx
            tall[i] = 1+ tall[tallest_idx]
            if tall[i] > tall[tallest_so_far]:
                tallest_so_far = i

        aaa = []
        cur = tallest_so_far
        while True:
            aaa.append(nums[cur])
            if cur==refs[cur]:
                break
            cur = refs[cur]

        return aaa

s = Solution()
print s.largestDivisibleSubset([1,2,3,4,6,7,12,13])
