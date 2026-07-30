class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispal(strr:str)->bool:
            l,r = 0,len(strr)-1
            while l<r:
                if strr[l] != strr[r]:
                    return False
                l+=1
                r-=1
            return True
        l,r = 0,len(s)-1
        while l<r:
            if s[l] != s[r]:
                return ispal(s[l+1:r+1]) or ispal(s[l:r])
            l+=1
            r-=1
        return True

        
        