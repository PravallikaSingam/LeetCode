class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables
        max_sum = nums[0]  # Stores the largest sum encountered
        current_sum = nums[0]  # Current subarray sum
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Update the current sum: either extend the current subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
        
        return max_sum

        