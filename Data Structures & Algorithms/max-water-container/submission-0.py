class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1

        maxArea = 0

        while left < right:
            current_area = (right - left) * min(heights[left],heights[right])

            maxArea = max(maxArea,current_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea

        

        