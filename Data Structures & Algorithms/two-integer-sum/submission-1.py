class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapping = {}

        for index in range(len(nums)):
            num1 = nums[index]
            num2 = target - num1
            if num2 in mapping:
                return [mapping[num2], index]
            mapping[num1] = index        