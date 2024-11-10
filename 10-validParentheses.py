class Solution:
    def isValid(self, s: str) -> bool:
        parentMap = {"[":"]", "{":"}", "(":")"}
        listParenthese = []

        if len(s) <2:
            return False

        for c in s:
            if len(listParenthese) == 0 and (c == ")" or c == "]" or c == "}" ):
                return False
                
            listParenthese.append(c)
           
            if c == ")" or c == "]" or c == "}" :
                if listParenthese.pop() != parentMap[listParenthese[-1]]:
                    return False
                else:
                    listParenthese.pop()

        return  len(listParenthese) == 0
    
s = Solution()
print(s.isValid("([])"))
print(s.isValid("(("))
