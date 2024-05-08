'''
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

'''


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = 0
        for index in range(len(digits)):
            number += digits[index] * int(f"1{str(0)* (len(digits) - index - 1)}")

        number += 1

        return [val for val in str(number)]


_ = Solution()

print(_.plusOne([4,5,3,2]))
        