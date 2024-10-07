
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        for i in range(n - 1):
            output[i + 1] = output[i] * nums[i]

            # print(output)

        # The above equals to
        # for i in range(n):
        #     if i == 0:
        #         continue
        #     output[i] = output[i-1] * nums[i-1]
        #     print(output)

        right = 1
        for i in range(n - 1, -1, -1):  # [4]: 3, 2, 1, 0
            # print(i)
            output[i] = output[i] * right
            right *= nums[i]

            # print(output)

        return output

# Another solution
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         output = [1] * n
#
#         left = 1
#         for i in range(n):
#             output[i] = output[i] * left
#             left *= nums[i]
#
#         right = 1
#         for i in range(n - 1, -1, -1):  # [4]: 3, 2, 1, 0
#             # print(i)
#             output[i] = output[i] * right
#             right *= nums[i]
#
#         return output