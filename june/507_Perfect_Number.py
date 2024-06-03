'''
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.



Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 7
Output: false


Constraints:

1 <= num <= 10^8

42



'''


# Check if the input is a prime number to reduce calculation queue

class Solution:
    def isPrimeNumber(self, num: int) -> bool:
        while True:
            if num < 10:
                if num == 2 or num == 3 or num == 5 or num == 7:
                    return True
                else:
                    return False

            num = sum([int(x) for x in str(num)])

    def checkPerfectNumber(self, num: int):
        if self.isPrimeNumber(num): return False
        if num == 1: return False

        total = 1

        for index in range(2, int(num**0.5) + 1):
            if num % index == 0:
                total += index + num//index

        return total == num


_ = Solution()
print(_.checkPerfectNumber(28))
