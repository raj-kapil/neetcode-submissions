class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        max_count = 0
        for num in nums:
            count = 1
            while (num -1) in set_:
                count += 1
                num = num - 1
            max_count = max(count, max_count)
        return max_count