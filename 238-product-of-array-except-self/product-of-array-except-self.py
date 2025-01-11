class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        output = [0] * len(nums)

        # Compute the left product array
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        # Compute the right product array
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Compute the final output array
        for i in range(len(nums)):
            output[i] = left[i] * right[i]

        return output


            

        