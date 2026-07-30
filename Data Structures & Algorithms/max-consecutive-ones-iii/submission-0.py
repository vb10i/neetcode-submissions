class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        maxlen = float('-inf')
        zeroes = 0
        n = len(nums)
        while r<n:
            if nums[r] == 0:
                zeroes += 1
            while zeroes>k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            if zeroes<=k:
                length = r-l+1
                maxlen = max(length, maxlen)
            r +=1
        return maxlen
