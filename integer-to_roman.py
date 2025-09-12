class Solution:
    def intToRoman(self, num: int) -> str:
        lookup = {
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
…                if v <= num:
                    output.append(k)
                    num -= v
                else:
                    break
        return "".join(output)
