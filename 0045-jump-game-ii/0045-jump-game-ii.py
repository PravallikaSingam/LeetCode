from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # No jumps needed if already at the last index

        jumps = 0        # Count of jumps
        current_end = 0  # Current maximum reachable index within a jump
        farthest = 0     # Farthest reachable index at any step

        for i in range(n - 1):
            # Update the farthest we can reach
            farthest = max(farthest, i + nums[i])

            # If we reach the end of the current jump range
            if i == current_end:
                jumps += 1  # Increment jump count
                current_end = farthest  # Move to the farthest index for the next jump

                # If we've already reached or passed the last index
                if current_end >= n - 1:
                    break

        return jumps

        