class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        # Iterate over the rest of the strings
        for string in strs[1:]:
            # Reduce the prefix until it matches the start of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""

        return prefix


        