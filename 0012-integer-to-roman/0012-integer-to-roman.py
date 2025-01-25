class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the Roman numeral values and their symbols in descending order
        values = [
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        ]
        symbols = [
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
        ]

        roman = ""
        # Iterate over the values and symbols
        for i in range(len(values)):
            # Append the Roman symbol as many times as it fits into num
            while num >= values[i]:
                roman += symbols[i]
                num -= values[i]
        
        return roman


        