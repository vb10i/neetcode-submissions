class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        subarrsum = 0
        minlen = 100001
        if target > sum(nums):
            return 0
        for r in range(len(nums)):
            subarrsum += nums[r]
            while subarrsum>=target:
                length = r-l+1
                minlen = min(minlen, length)
                subarrsum -= nums[l]
                l += 1
        return minlen
                
