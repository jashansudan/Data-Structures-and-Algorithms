class Solution(object):
    def productExceptSelf(self, nums):
        multSoFar = 1
        product = []
        for i in range(len(nums)):
            product.append(multSoFar)
            multSoFar *= nums[i]
        multSoFar = 1
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= multSoFar
            multSoFar *= nums[i]
        return product
