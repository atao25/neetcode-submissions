class Solution:
    def isValid(self, s: str) -> bool:
        
        # 1. brute force 
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
        

        # 2. stack (LIFO)