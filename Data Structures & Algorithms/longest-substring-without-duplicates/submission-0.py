class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp = {}
        l = 0
        maxlen = 0
        maxfreq = 0
        for r in range(len(s)):
            mapp[s[r]] = mapp.get(s[r], 0)+1
            while mapp[s[r]]>1:
                mapp[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r-l+1)
        return maxlen
            