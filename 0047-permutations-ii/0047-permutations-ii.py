from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort the array to easily skip duplicates

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])  # Add a copy of the current permutation
                return

            for i in range(len(nums)):
                # Skip already used numbers or duplicates
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue

                # Mark the number as used and recurse
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                # Backtrack by undoing the changes
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result

        