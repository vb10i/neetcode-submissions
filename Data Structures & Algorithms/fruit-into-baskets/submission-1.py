class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r = 0,0
        n = len(fruits)
        mapp = defaultdict(int)
        maxlen = 0

        for i in range(len(fruits)):
            mapp[fruits[i]] += 1

            while len(mapp)>2:
                mapp[fruits[l]] -= 1
                if mapp[fruits[l]] == 0:
                    mapp.pop(fruits[l])
                l += 1
            maxlen = max(maxlen, i-l+1)
        return maxlen
        



                