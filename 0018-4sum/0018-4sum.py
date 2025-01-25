class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()  # Sort the array to make it easier to find unique quadruplets
        result = []

        # Iterate through the array with the first pointer
        for i in range(len(nums) - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Iterate with the second pointer
            for j in range(i + 1, len(nums) - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Use two pointers for the third and fourth numbers
                left, right = j + 1, len(nums) - 1

                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        # If we found a valid quadruplet, add it to the result
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for the third and fourth numbers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Move the pointers inward
                        left += 1
                        right -= 1

                    elif current_sum < target:
                        left += 1  # Increase the sum by moving the left pointer
                    else:
                        right -= 1  # Decrease the sum by moving the right pointer

        return result

        