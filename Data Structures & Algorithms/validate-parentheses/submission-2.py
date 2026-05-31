class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        dict_ = {")": "(", "}": "{", "]": "["}

        close_ = dict_.keys()
        open_ = dict_.values()

        index = 1
        if s[0] in close_:
            return False
        stack = deque()

        for i in range(len(s)):
            if s[i] in open_:
                stack.append(s[i])
            else:
                if stack and dict_[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return False if stack else True
