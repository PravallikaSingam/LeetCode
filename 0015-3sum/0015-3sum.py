class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort the array to facilitate two-pointer approach
        n = len(nums)
        result = []
        
        for i in range(n):
            # Avoid duplicates for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer approach
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Avoid duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move the pointers after finding a valid triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # Increase the sum
                else:
                    right -= 1  # Decrease the sum
        
        return result

        