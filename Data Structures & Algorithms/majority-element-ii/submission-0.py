class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numsdict = {}
        for n in nums: 
            numsdict[n] = numsdict.get(n,0)+1 #num,times
        res = []
        for n,t in numsdict.items():
            if t>len(nums)/3:
                res.append(n)
        return res     