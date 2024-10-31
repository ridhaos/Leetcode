# Check if Int is palindrome without converting to String
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        x1 = x
        if x < 0:
            return False
        
        while x1 > 0:
            y = ((y<<3) + (y<<1)) + (x1 % 10)
            x1 = x1 // 10
            
        print(y)
        if y == x:
            return True
        else:
            return False

        

s = Solution()
print(s.isPalindrome(11))