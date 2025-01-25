class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a DP table where dp[i][j] indicates if s[:i] matches p[:j]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True  # Empty string matches empty pattern

        # Handle patterns like a*, a*b*, etc., that can match an empty string
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    # Current characters match
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Zero occurrences of the preceding element OR
                    # One or more occurrences of the preceding element
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

        return dp[len(s)][len(p)]
