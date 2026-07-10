class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []

        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i -1]:
                continue
            
            fptr = i + 1
            sptr = len(arr) - 1

            while fptr < sptr:
                curr_sum = arr[i] + arr[fptr] + arr[sptr]
                if curr_sum < 0:
                    fptr += 1
                elif curr_sum > 0:
                    sptr -= 1
                else:
                    result.append([arr[i], arr[fptr], arr[sptr]])
                    fptr += 1
                    while fptr < sptr and arr[fptr] == arr[fptr-1]:
                        fptr += 1
        return result