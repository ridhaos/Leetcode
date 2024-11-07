# Here You find my leetcode problem Solution:

In this repository i share with you my solution for 
leetcode problems where i enjoyed to solve them and improve my knowledge in algorithm by challenging my self to resolve these problem and calculate complexity for each problem.

***All solution are written in Python language using basic python library***


## 1. Median of Two Arrays:
1) **Problem:**
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
2) **Solution:**
For this solution i'm merging the two arrays to one and sorted after
using python sort default function which is O(nlog(n)) and after check if length of merge array is even or odd and return back the median.

## 2. ZigZag text transform:
1) **Problem:**
For this solution i'm merging the two arrays to one and sorted after
using python sort default function which is O(nlog(n)) and after check if length of merge array is even or odd and return back the median.
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

`P   A   H   N`

`A P L S I I G`

`Y   I   R`

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
2) **Solution:**
For this solution i'm transform the input text to column.
This solution takes O(n) : number of characters + O(m) string copy as strings are immutable.

## 3. Reverse integer:
1) **Problem:**
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
2) **Solution:**
For this solution im dividing the integer by 10 and append the rest to array,
so we get reverse number and check if negative if it multiplied by -1.
it takes O(log(n)) and n is the digit number.

## 4. String To integer transform (atoi()):
1) **Problem:**
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
- Whitespace: Ignore any leading whitespace (" ").
- Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
- Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
- Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
2) **Solution:**
For this solution im going throw the string and check characther by character if is digit or no.
if it's pushed to int by shifting the number by 10, The complexity is O(n) n is the number of characters in input string.

## 5. Longest Palindrome for String:
1) **Problem:**
Given a string s, return the longest palindromic substring in s.
2) **Solution:**
Use *Manacher's algorithm* which is the best algorithm for this kind of problems with complexity O(n).

## 6. Longest Palindrome for String:
1) **Problem:**
Given an integer x, return true if x is a palindrome and false otherwise,
Without converting the number to string.
2) **Solution:**
For this problem im reversing the number and check if input number equal to reverse number:
input = 12621 to check if palindrome the reverse number of this must be equal to it.
Complexity is O(n): n number of digit.

## 7. Regular Expression Matching:
1) **Problem:**
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
2) **Solution:**
For this solution im using Dynamic Programing Algorithm, which is very famous for this kind
of problem.
Check here for more explication:
https://stackoverflow.com/questions/49572289/understanding-regex-string-matching-using-dynamic-programming


## 8. Convert to Roman Integer:
1) **Problem:**
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.
2) **Solution:**
Solution for this program first i created a Map for all Roman number.
Secondly i divide the number into digits and stock in List.
Using List index to get the tenth or hundredth, ...
and after using map to choose between corresponding map number and stocked the result in string
list.
Time Complexity is O(n).