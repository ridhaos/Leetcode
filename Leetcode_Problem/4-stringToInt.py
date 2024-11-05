# ASCII table 30 = 0 ... and 39 = 9
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) <= 0 or len(s) >= 200:
            return 0
         
        neg = False
        number = 0
        count = 0

        for i in range(len(s)):
            if s[i] == ' ':
                count += 1
            else :
                break

        for c in range(count, len(s)):
            if s[c] == '-' and c == count:
                neg = True
                continue

            elif s[c] == '+' and c == count:
                continue

            elif ord(s[c]) >= ord('0') and ord(s[c]) <= ord('9'):
                if number == 0:
                    number = ord(s[c]) - ord('0')
                else:
                    number = Solution.shiftNumberToLeft(number)
                    number += ord(s[c]) - ord('0')

            else:
                break;

        number = number * -1 if neg else number
        
        return Solution.checkNumberBorder(number)

    def shiftNumberToLeft(x: int) -> int:
        return (x<<3) + (x<<1)
    
    def checkNumberBorder(x: int) -> int:
        if x >= 2**31 :
            x = 2**31 -1
        elif x < -2**31:
            x = -2**31
    

s = Solution()
print(s.myAtoi("   +0 123"))
# print(s.myAtoi("-91283472332"))