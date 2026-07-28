class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums) #{2, 3, 4, 5, 10, 20}
        longest, length = 0,0
        res = []
        for n in nums:
            if n-1 not in nset:
                length = 1
                while (n+length) in nset:
                    length += 1
                longest = max(longest, length)
        return longest
