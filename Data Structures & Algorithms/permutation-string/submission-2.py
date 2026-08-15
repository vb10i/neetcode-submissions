class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp = {}
        if len(s1)>len(s2):
            return False
        l = 0
        for ele in s1:
            mapp[ele] = mapp.get(ele, 0)+1
            
        for r in range(len(s2)):
            if s2[r] in mapp:
                mapp[s2[r]] -= 1
            if r-l+1 > len(s1):
                if s2[l] in mapp:
                    mapp[s2[l]] += 1
                l += 1
            if r-l+1 == len(s1):
                for v in mapp.values():
                    if v != 0:
                        break
                else:
                    return True
        return False 
            