from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        current_count = Counter()

        left = 0
        min_len = float('inf')
        min_window = ""
        required = len(t_count)
        formed = 0

        for right in range(len(s)):
            char = s[right]
            current_count[char] += 1

            if char in t_count and current_count[char] == t_count[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]

                left_char = s[left]
                current_count[left_char] -= 1
                if left_char in t_count and current_count[left_char] < t_count[left_char]:
                    formed -= 1

                left += 1

        return min_window
