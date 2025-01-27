from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  # Narrow to the left half for the first occurrence
                    else:
                        left = mid + 1  # Narrow to the right half for the last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return bound

        start = findBound(isFirst=True)
        if start == -1:
            return [-1, -1]  # Target not found

        end = findBound(isFirst=False)
        return [start, end]

        