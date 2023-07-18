class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVal = 0
        i,j =0,len(height)-1

        while i<j:
            area = (j-i)*min(height[i],height[j])
            maxVal = max(maxVal, area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        
        return maxVal