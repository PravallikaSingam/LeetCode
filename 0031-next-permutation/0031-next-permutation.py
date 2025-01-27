class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If such an element is found, find the element just larger than it to the right
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap the two elements
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the subarray to the right of the first decreasing element
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
