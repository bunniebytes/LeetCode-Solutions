class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = (num // 1000) % 10
        hundreds = (num // 100) % 10
        tens = (num // 10) % 10
        ones = num % 10
        results = ""

        if thousands:
            results +="M" * thousands
        if hundreds:
            if hundreds == 4:
                results += "CD"
            elif hundreds == 9:
                results += "CM"
            elif hundreds >= 5:
                results += "D" + ("C" * (hundreds % 5))
            else:
                results += "C" * hundreds
        if tens:
            if tens == 4:
                results += "XL"
            elif tens == 9:
                results += "XC"
            elif tens >= 5:
                results += "L" + ("X" * (tens % 5))
            else:
                results += "X" * tens
        if ones:
            if ones == 4:
                results += "IV"
            elif ones == 9:
                results += "IX"
            elif ones >= 5:
                results += "V" + ("I" * (ones % 5))
            else:
                results += "I" * ones

        return results