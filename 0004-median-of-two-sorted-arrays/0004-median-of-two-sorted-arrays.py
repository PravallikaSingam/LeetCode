from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        # Binary search on the smaller array
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # Partition in nums1
            j = half - i            # Partition in nums2

            # Values around the partition
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')

            # Check if partitions are valid
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Found correct partition
                if total % 2 == 0:  # Even total elements
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:  # Odd total elements
                    return min(nums1_right, nums2_right)
            elif nums1_left > nums2_right:
                # Move partition in nums1 to the left
                right = i - 1
            else:
                # Move partition in nums1 to the right
                left = i + 1
        
        raise ValueError("Input arrays are not valid")

# Example usage
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
        