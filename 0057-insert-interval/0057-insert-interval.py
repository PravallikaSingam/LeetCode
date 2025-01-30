from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort intervals based on the start value
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If merged list is empty or no overlap, append interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge overlapping intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result

        