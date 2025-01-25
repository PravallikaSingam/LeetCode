class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to track the number of elements that are not equal to val
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Place the non-val element at the k-th position
                k += 1  # Increment k for the next unique element
        
        return k  # The number of elements not equal to val
nums = []
solution = Solution()
print(solution.removeElement(nums, 3))  # Output: 0
nums = [1, 2, 3, 4]
solution = Solution()
print(solution.removeElement(nums, 5))  # Output: 4, nums = [1, 2, 3, 4]
nums = [3, 3, 3, 3]
solution = Solution()
print(solution.removeElement(nums, 3))  # Output: 0


        