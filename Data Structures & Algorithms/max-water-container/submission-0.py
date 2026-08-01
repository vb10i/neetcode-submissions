class Solution:
    def maxArea(self, height: List[int]) -> int:
        # MISTAKE I DID: DONT FIND MAX HEIGHT FROM BOTH END, FIND WATER FOR EVERYONE AND KEEP COMPARING 
        l,r = 0, len(height)-1
        maxl, maxr = height[l], height[r]
        dis = r-l
        water = 0
        while l<r:
            dis = r-l
            total = dis*min(height[l],height[r])
            water = max(water, total)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return water 