# Brute Force

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        # Iterate through all possible pairs of bars
        for i in range(n):
            for j in range(i, n):
                # Calculate the height of the rectangle (minimum height of bars in the range)
                min_height = min(heights[i:j+1])

                # Calculate the width of the rectangle
                width = j - i + 1

                # Calculate the area of the rectangle
                area = min_height * width

                # Update the maximum area if the current rectangle has a larger area
                max_area = max(max_area, area)

        return max_area


# Monotonic Stack -1 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        # Iterate through each index and height in the heights array
        for index, height in enumerate(heights):
            start = index

            # Check if the stack is not empty and the height at the top of the stack is greater than the current height
            while start and stack[-1][1] > height:
                i, h = stack.pop()
                # Calculate the area for the popped element and update maxArea if needed
                maxArea = max(maxArea, (index - i) * h)
                start = i

            # Push the current index and height onto the stack
            stack.append((start, height))

        # Process any remaining elements in the stack
        for index, height in stack:
            maxArea = max(maxArea, (len(heights) - index) * height)

        return maxArea

# Monotonic Stack-2
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            # If the current height is smaller than the height of the bar at the top of the stack,
            # calculate the area of the rectangle formed by the bar at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        # Process the remaining bars in the stack
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area
