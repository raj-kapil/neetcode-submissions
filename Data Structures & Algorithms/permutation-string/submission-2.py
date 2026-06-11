class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def get_char_arr(s):
            char_arr = [0] * 26
            for i in s:
                char_arr[ord(i) - ord('a')] += 1
            return char_arr

        if len(s1) > len(s2):
            return False

        s1_arr = get_char_arr(s1)
        window_arr = get_char_arr(s2[:len(s1)])
        if s1_arr == window_arr:
            return True

        fptr = 1
        for i in range(len(s1), len(s2)):
            window_arr[ord(s2[i]) - ord('a')] += 1
            window_arr[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_arr == window_arr:
                return True

        return False
                    



            