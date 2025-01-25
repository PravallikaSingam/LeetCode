class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        # Mapping of digits to letters, similar to a telephone keypad
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # Initialize the result with the letters of the first digit
        result = ['']

        # Iterate through each digit in the input string
        for digit in digits:
            letters = digit_to_letters[digit]
            result = [prefix + letter for prefix in result for letter in letters]

        return result

        