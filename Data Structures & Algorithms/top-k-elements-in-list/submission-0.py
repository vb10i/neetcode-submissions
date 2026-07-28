class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsdict = {}
        for n in nums:
            numsdict[n] = numsdict.get(n,0)+1
        val, output = 0, []
        while k!=0:
            val = max(numsdict, key=numsdict.get)
            output.append(val)
            numsdict.pop(val)
            k -= 1
        return output 