class Solution:
    def reverse(self, x: int) -> int:
        if x > (2**31)-1 or x < (-2**31):
            return 0
        l=[]
        count=0
        neg=False
        if x <0:
            x *= -1
            neg = True
        while x>0:
            l.append(x%10)
            x = x//10
            count+=1
        while count > 0:
            x += (10 ** (count -1)) * l[-(count)]
            count-=1
        
        if x > (2**31)-1 or x < -2**31:
            return 0
        return x*-1 if neg else x


s1 = Solution()

print(s1.reverse(1230))
print(s1.reverse(-83493))

