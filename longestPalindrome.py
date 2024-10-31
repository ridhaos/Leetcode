class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Step 1: Transform the string
        T = "#" + "#".join(s) + "#"  # Add delimiters
        n = len(T)
        P = [0] * n  # Array to store palindrome radii
        C = R = 0    # Current center and right boundary

        # Step 2: Process the transformed string
        for i in range(n):
            # Find the mirrored index of i with respect to center C
            mirror = 2 * C - i

            # Step 3: Use previously computed palindrome information
            if i < R:
                P[i] = min(R - i, P[mirror])

            # Step 4: Expand around center i
            while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1

            # Step 5: Update the center and right boundary if needed
            if i + P[i] > R:
                C = i
                R = i + P[i]

        # Step 6: Extract all palindromic substrings
        palindromic_substrings = []
        max = 0
        for i in range(n):
            # Extract palindromic substrings for each center i
            length = P[i]
            if length > max:
                max = length
                start = (i - length) // 2  # Convert to the original string's indices
                palindromic_substrings = s[start: start + length]


        return palindromic_substrings 
    

s = Solution()

print(s.longestPalindrome("abaabccba"))
print(s.longestPalindrome("abaaxabaxccba"))
