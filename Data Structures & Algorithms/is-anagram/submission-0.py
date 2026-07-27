class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict, tdict = {}, {}
        for ch in s:
            sdict[ch] = sdict.get(ch,0)+1 # ch, times
            
        for ch in t:
            tdict[ch] = tdict.get(ch,0)+1


        return sdict == tdict
