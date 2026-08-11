class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        while left < right:
            while not self.isAllowed(s[left]) and left < right:
                left += 1
            while not self.isAllowed(s[right]) and left < right:
                right -= 1
            
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True
    
    def isAllowed(self, char: str) -> bool:
        num = ord(char)
        return (ord("A") <= num <= ord("Z")) or (ord("a") <= num <= ord("z")) or (ord("0") <= num <= ord("9"))