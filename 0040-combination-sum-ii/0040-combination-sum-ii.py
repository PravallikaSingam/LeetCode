from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort candidates to handle duplicates

        def backtrack(remaining, combination, start):
            # If the remaining target is 0, we found a valid combination
            if remaining == 0:
                result.append(list(combination))
                return

            # Explore further by iterating through candidates
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current = candidates[i]
                # Stop further exploration if the current candidate exceeds the remaining target
                if current > remaining:
                    break

                # Include the current candidate and explore further
                combination.append(current)
                backtrack(remaining - current, combination, i + 1)  # Move to the next element
                # Backtrack by removing the last added element
                combination.pop()

        backtrack(target, [], 0)
        return result

        