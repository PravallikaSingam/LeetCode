from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Helper function for backtracking
        def backtrack(start=0):
            # If the start index is equal to the length of nums, a permutation is complete
            if start == len(nums):
                result.append(nums[:])  # Add a copy of the current permutation
                return

            for i in range(start, len(nums)):
                # Swap the current element with the starting element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse with the next element
                backtrack(start + 1)
                # Backtrack by undoing the swap
                nums[start], nums[i] = nums[i], nums[start]

        backtrack()
        return result

        