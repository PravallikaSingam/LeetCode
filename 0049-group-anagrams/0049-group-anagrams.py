from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Hash map to group anagrams

        for word in strs:
            # Sort the word to use it as a key
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())

        