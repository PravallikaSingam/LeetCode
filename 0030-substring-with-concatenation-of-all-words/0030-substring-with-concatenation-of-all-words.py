from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        # Initialize variables
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)  # Frequency count of words
        result = []
        
        # Loop through the string for possible starting points
        for i in range(word_len):
            left = i
            right = i
            current_freq = Counter()
            count = 0
            
            while right + word_len <= len(s):
                # Extract a word from the substring
                word = s[right:right + word_len]
                right += word_len
                
                # Check if it is a valid word
                if word in word_freq:
                    current_freq[word] += 1
                    count += 1
                    
                    # If the word frequency exceeds, slide the window
                    while current_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # Check if the current window contains all words
                    if count == word_count:
                        result.append(left)
                else:
                    # If the word is invalid, reset the window
                    current_freq.clear()
                    count = 0
                    left = right
        
        return result

        