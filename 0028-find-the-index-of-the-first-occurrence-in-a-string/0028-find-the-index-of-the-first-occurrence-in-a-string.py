class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if the needle is empty
        if not needle:
            return 0

        # Use Python's built-in string method to find the index of the first occurrence
        index = haystack.find(needle)
        
        return index

        