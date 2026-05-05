class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open=  { 
            "}": "{",
             ")": "(",
              "]": "["
              }

        # build a stack 
        stack = []
        # check if bracket is in the s (list)
        for bracket in s:
            # ONLY CHECKS KEYS - if bracket is in the close to open then = closing bracket
            if bracket in close_to_open:
                # checks if stack is empty 
                if not stack:
                    return False
                # take last element off of the stack 
                top = stack.pop()
                # if the last element is not the same as the close_to_open then False
                if close_to_open[bracket] != top:
                    return False

            else:
                stack.append(bracket)
        
        if stack:
            return False
        else:
            return True

        