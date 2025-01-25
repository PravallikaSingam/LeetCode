class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            # Expand around the center as long as it's a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindromic substring
            return s[left + 1:right]
        
        # Edge case: if the string is empty or has only one character
        if len(s) <= 1:
            return s

        longest = ""
        for i in range(len(s)):
            # Odd-length palindromes (single character center)
            odd_palindrome = expand_around_center(i, i)
            # Even-length palindromes (two-character center)
            even_palindrome = expand_around_center(i, i + 1)

            # Update the longest palindrome if necessary
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest

# Example usage
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   # Output: "bb"

        