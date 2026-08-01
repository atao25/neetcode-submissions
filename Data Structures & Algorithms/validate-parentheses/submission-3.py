class Solution:
    def isValid(self, s: str) -> bool:
        
        # 1. brute force 
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''
        

        # 2. stack (LIFO)
        stack = []
        # create dictionary
        pairs = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }

        for c in s:
            if c not in pairs:
                stack.append(c)
            
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            
        return not stack # stack empty

       
       

