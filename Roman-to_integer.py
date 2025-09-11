class Solution:
    def romanToInt(self, s: str) -> int:
        summ = prev = 0
        dictt = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for char in reversed(s):
            value = dictt[char]
            if value < prev:
                summ -= value
            else:
                summ += value
            prev = value
        return summ
