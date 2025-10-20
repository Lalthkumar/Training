import sys

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        dvd = abs(dividend)
        dvs = abs(divisor)
        result = 0
        while dvd >= dvs:
            temp = dvs
            multiple = 1
            while dvd >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dvd -= temp
            result += multiple
        return sign * result

if __name__ == "__main__":
    dividend = int(sys.argv[1])
    divisor = int(sys.argv[2])
    sol = Solution()
    print(sol.divide(dividend, divisor))
