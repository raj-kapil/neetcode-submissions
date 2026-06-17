class Solution:
    def maxArea(self, arr: List[int]) -> int:
        left = 0 
        right = len(arr) - 1

        max_water = 0
        while left < right:
            max_height = min(arr[left], arr[right])
            max_water = max(max_water, max_height * (right - left))
            if arr[left] >= arr[right]:
                right -= 1
            else:
                left += 1
            
        return max_water