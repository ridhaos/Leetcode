class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = [""]*numRows
        h = 0
        tbr = False
        for c in s:
            if h == 0 or h == numRows-1:
                tbr = not tbr
            l[h] += c
            if tbr:
                h+=1
            else:
                h-=1
        return ''.join(l)

s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))