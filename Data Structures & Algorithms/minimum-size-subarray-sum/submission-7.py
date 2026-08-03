class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        temp = 0
        if sum(nums)<target:
            return 0
        minlen = 100001
        for r in range(len(nums)):
            temp += nums[r]
            while temp>=target:
                length = r-l+1
                minlen = min(length, minlen)
                temp -= nums[l]
                l += 1
        return minlen 

                 