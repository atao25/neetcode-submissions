class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 1. brute force: reverse string

        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
            
        return newStr == newStr[::-1]