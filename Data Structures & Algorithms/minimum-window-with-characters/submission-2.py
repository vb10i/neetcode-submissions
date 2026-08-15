class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map1= {}
        for ele in t:
            map1[ele] = map1.get(ele, 0)+1
        l = 0
        L,R = 0,0
        minlen = 100001
        if len(s)<len(t):
            return ""
        for r in range(len(s)):
            if s[r] in map1:
                map1[s[r]] -= 1
            while all(v<=0 for v in map1.values()):
                if r-l+1<minlen:
                    minlen = r-l+1
                    L,R = l,r
                if s[l] in map1:
                    map1[s[l]] += 1
                l += 1
        if minlen == 100001:
            return ""
        return s[L:R+1]