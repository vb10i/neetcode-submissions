class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsdict = {}
        for n in nums:
            numsdict[n] = numsdict.get(n, 0) + 1 # num, times
        
        for n,t in numsdict.items():
            if t>1:
                return True
        return False