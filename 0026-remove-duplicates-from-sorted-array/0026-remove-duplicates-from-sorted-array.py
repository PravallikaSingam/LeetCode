class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0  # Pointer to track where the next unique element should go
        
        # Start from the second element and traverse the array
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # When a new unique element is found
                i += 1  # Move the slow pointer
                nums[i] = nums[j]  # Update the value at the slow pointer
        
        # Return the count of unique elements
        return i + 1
nums = []
solution = Solution()
print(solution.removeDuplicates(nums))  # Output: 0
nums = [5, 5, 5, 5, 5]
solution = Solution()
print(solution.removeDuplicates(nums))  # Output: 1, nums = [5, _, _, _, _]
nums = [1, 2, 3, 4]
solution = Solution()
print(solution.removeDuplicates(nums))  # Output: 4, nums = [1, 2, 3, 4]

        