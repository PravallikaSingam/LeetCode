class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        # Initialize the start of the window and the maximum length
        start = 0
        max_length = 0

        for end in range(len(s)):
            # If the character is already in the current window, move the start pointer
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            
            # Update the character's last seen index
            char_index[s[end]] = end
            
            # Update the maximum length of the substring
            max_length = max(max_length, end - start + 1)
        
        return max_length
        
        