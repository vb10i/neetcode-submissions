class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # len - maxfreq <= K
        l,r = 0,0
        maxlen = 0
        mapp = {}
        maxfreq = 0
        for r in range(len(s)):
            mapp[s[r]] = mapp.get(s[r], 0)+1
            maxfreq = max(maxfreq, mapp[s[r]])
            while (r-l+1)-maxfreq > k:
                mapp[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r-l+1)
        return maxlen 

