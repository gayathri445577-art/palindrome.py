class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reverse = 0
        if x<0:
            return False
        while x != 0:
            remainder = x % 10
            reverse = reverse * 10 + remainder
            x = x // 10
        if reverse == original:
            return True
        else:
            return False
