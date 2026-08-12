class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        m = len(nums)//2
        L = nums[:m]
        R = nums[m:]
        L = self.sortArray(L)
        R = self.sortArray(R)
        Llen, Rlen = len(L), len(R)
        res = [0]*len(nums)
        i = 0
        l,r = 0,0
        while l<Llen and r<Rlen:
            if L[l] < R[r]:
                res[i] = L[l]
                l += 1
            else:
                res[i] = R[r]
                r += 1
            i += 1
        while l<Llen:
            res[i] = L[l]
            l += 1
            i += 1
        while r<Rlen:
            res[i] = R[r]
            r += 1
            i += 1
        return res 