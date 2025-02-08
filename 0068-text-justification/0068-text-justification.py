from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, line_length = [], 0

        for word in words:
            # Check if adding another word exceeds maxWidth
            if line_length + len(line) + len(word) > maxWidth:
                # Distribute spaces
                spaces = maxWidth - line_length
                for i in range(spaces):
                    line[i % (len(line) - 1 or 1)] += ' '
                res.append(''.join(line))
                line, line_length = [], 0

            line.append(word)
            line_length += len(word)

        # Last line: Left-justified
        last_line = ' '.join(line).ljust(maxWidth)
        res.append(last_line)

        return res

        