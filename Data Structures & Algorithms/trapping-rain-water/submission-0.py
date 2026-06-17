class Solution:
    def trap(self, arr: List[int]) -> int:
        if not arr:
            return 0

        fptr = 0
        sptr = len(arr) - 1

        left_max = arr[fptr]
        right_max = arr[sptr]

        water = 0

        while fptr < sptr:
            if left_max < right_max:
                fptr += 1
                left_max = max(left_max, arr[fptr])

                water += left_max - arr[fptr]
            else:
                sptr -= 1
                right_max = max(right_max, arr[sptr])
                water += right_max - arr[sptr]
        
        return water

        
            

