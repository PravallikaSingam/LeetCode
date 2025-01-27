from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remaining, combination, start):
            # If the remaining target is 0, we found a valid combination
            if remaining == 0:
                result.append(list(combination))
                return

            # Explore further by iterating through candidates
            for i in range(start, len(candidates)):
                current = candidates[i]
                # Skip if the current candidate exceeds the remaining target
                if current > remaining:
                    continue

                # Include the current candidate and explore further
                combination.append(current)
                backtrack(remaining - current, combination, i)  # Not i + 1 because we can reuse the same element
                # Backtrack by removing the last added element
                combination.pop()

        backtrack(target, [], 0)
        return result

        