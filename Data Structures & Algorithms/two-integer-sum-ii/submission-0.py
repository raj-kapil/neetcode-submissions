class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        fptr = 0 
        sptr = len(numbers) - 1

        while fptr < sptr:
            curr_sum = numbers[fptr] + numbers[sptr]
            if curr_sum < target:
                fptr += 1
            elif curr_sum > target:
                sptr -=1 
            else:
                return [fptr+1, sptr+1]
        
        