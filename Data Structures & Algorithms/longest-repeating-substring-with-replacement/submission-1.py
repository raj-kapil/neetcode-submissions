class Solution:
    def characterReplacement(self, arr: str, k: int) -> int:
                
        fptr = 0
        max_len = 0
        max_count = 0
        char_freq = {}

        for i in range(len(arr)):
            current_char = arr[i]
            if current_char in char_freq:
                char_freq[current_char] += 1
            else:
                char_freq[current_char] = 1

            max_count = max(max_count, char_freq[current_char])
            while (i - fptr + 1 - max_count) > k:
                char_freq[arr[fptr]] -= 1
                fptr += 1

            max_len = max(max_len, i - fptr +1)
        return max_len
