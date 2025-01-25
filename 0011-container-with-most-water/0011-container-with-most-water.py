class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Initialize two pointers and the maximum area
        left, right = 0, len(height) - 1
        max_area = 0

        # Move the pointers towards each other
        while left < right:
            # Calculate the area with the current left and right pointers
            width = right - left
            current_area = min(height[left], height[right]) * width
            # Update the maximum area if the current one is larger
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


        