class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        temp_dict = {}
        for index, num in enumerate(nums):
            second_ele = target - num
            if second_ele in temp_dict:
                return [temp_dict[second_ele], index]
            temp_dict[num] = index 
        return [-1.-1]
