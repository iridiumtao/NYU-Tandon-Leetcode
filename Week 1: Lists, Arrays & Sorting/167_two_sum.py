from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        L, R = 0, 1
        R_max = False
        len_numbers = len(numbers)

        while (L < R):
            if numbers[L] + numbers[R] == target:
                return [L + 1, R + 1]
            elif numbers[L] + numbers[R] < target and R_max is False:
                if R == len_numbers - 1:
                    R_max = True
                else:
                    R += 1
            elif numbers[L] + numbers[R] > target:
                R_max = True
                R -= 1

            elif numbers[L] + numbers[R] < target and R_max is True:
                L += 1