class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = nums.count(0) # zeros
        o = nums.count(1) # ones
        t = nums.count(2) # twos

        for i in range(z):
            nums[i] = 0

        for i in range(z, z+o):
            nums[i] = 1

        for i in range(z+o, z+o+t):
            nums[i] = 2