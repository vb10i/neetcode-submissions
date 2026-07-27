class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsdict = {}
        for n in nums:
            numsdict[n] = numsdict.get(n, 0)+1
        maxnum = 0
        for n,t in numsdict.items():
            if t > len(nums)/2:
                maxnum = n
        return maxnum