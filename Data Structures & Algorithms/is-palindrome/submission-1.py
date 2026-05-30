class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_string = ''
        for char in s:
            if char.isalnum():
                reverse_string += char.lower()
        return reverse_string[::-1] == reverse_string

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = ''
#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
#         return newStr == newStr[::-1]