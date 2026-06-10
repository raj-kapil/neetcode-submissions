class Solution:
    def lengthOfLongestSubstring(self, arr: str) -> int:
                
        fptr = 0 
        char_freq = {}
 
        max_len = 0

        for i in range(len(arr)):
            word = arr[i]
            
            if word in char_freq:
                char_freq[word] += 1
                while char_freq[word] > 1:
                    char_freq[arr[fptr]] -= 1
                    if char_freq[arr[fptr]] == 0:
                        del char_freq[arr[fptr]]
                    fptr += 1
            else:
                char_freq[word] = 1
                
            max_len = max(max_len, i - fptr + 1)
        return max_len