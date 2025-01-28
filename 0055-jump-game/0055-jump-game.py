class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0  # Track the farthest index reachable
        n = len(nums)
        
        for i in range(n):
            # If the current index is beyond the farthest reachable index, return False
            if i > farthest:
                return False
            
            # Update the farthest reachable index
            farthest = max(farthest, i + nums[i])
            
            # If we can reach or exceed the last index, return True
            if farthest >= n - 1:
                return True
        
        return False
