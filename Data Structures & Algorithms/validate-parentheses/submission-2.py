class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char not in bracket_map:
                stack.append(char)
                continue
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        return not stack