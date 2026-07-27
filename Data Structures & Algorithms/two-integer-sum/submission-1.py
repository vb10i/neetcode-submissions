class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indx = {}
        for i,n in enumerate(nums):
            indx[n] = i #num, index
        for i,n in enumerate(nums):
            diff = target - n
            if diff in indx and indx[diff] != i: # after 'and' case --> to not check same number twice
                return [i, indx[diff]]
        return []