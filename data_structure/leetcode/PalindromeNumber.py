class Solution:
    def isPalindrome(self, x: int) -> bool:
        if list(str(x)) == list(str(x))[::-1]:
            return True
        return False
