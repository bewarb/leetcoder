class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]

                width= i if not stack else i - stack[-1] -1

                area = height * width
                maxArea = max(maxArea, area)

            stack.append(i)

        while stack:
            height = heights[stack.pop()]

            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            area = height * width
            maxArea = max(maxArea, area)

        return maxArea
