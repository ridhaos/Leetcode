class Solution:
    roman_num = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}

    def intToRoman(self, num: int) -> str:
        runL = []
        # Sperate numbers
        while num > 0:
            runL.append(num % 10)
            num = num // 10
            
        romanNum = []
        # use list index to get tenth, hundredth, ...
        j = 1
        for i in range(0, len(runL)):
            if runL[i] == 9:
                romanNum.insert(0, Solution.roman_num[j]+Solution.roman_num[(j*10)])
            elif runL[i] == 4:
                romanNum.insert(0, Solution.roman_num[j]+Solution.roman_num[(j*5)])
            elif runL[i] >= 5:
                romanNum.insert(0, Solution.roman_num[j*5]+((runL[i]-5)*Solution.roman_num[j]))
            else:
                romanNum.insert(0, runL[i] * Solution.roman_num[j])
            j *= 10


        return ''.join(romanNum)
        # print(romanNum)

    
    
    
s = Solution()
print(s.intToRoman(3749))