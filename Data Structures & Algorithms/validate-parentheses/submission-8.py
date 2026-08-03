class Solution:
    def isValid(self, s: str) -> bool:
        valid_stack = []
        char_map = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in char_map:
                if valid_stack and char_map[c] == valid_stack[-1]:
                    valid_stack.pop()
                else:
                    return False
            else:
                valid_stack.append(c)
        return True if not valid_stack else False
