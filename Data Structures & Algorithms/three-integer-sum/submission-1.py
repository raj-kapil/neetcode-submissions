class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            fptr = i + 1
            sptr = len(nums) - 1
            while fptr < sptr:
                curr_sum = nums[i] + nums[fptr] + nums[sptr]
                if curr_sum > 0:
                    sptr -= 1
                elif curr_sum < 0:
                    fptr += 1
              
                else:
                    result.append([nums[i] , nums[fptr] , nums[sptr]])
                    fptr += 1
                    while fptr < sptr and nums[fptr] == nums[fptr - 1]:
                        fptr += 1
                    
        return result
            