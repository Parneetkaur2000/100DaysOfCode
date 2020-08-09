Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty-seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
Example 1:
Input: 3
Output: "III"
Example 2:
Input: 4
Output: "IV"
Example 3:
Input: 9
Output: "IX"
Example 4:
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

******************************



def num_conversion(input_number):
  
  if input_number <= 0: 
    return None
  dict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
  vals = sorted(dict.keys(), reverse=True)
  roman = ''
  for val in vals:
    n, input_number = divmod(input_number, val)
    last_digit = roman[-1] if len(roman) > 0 else ''
    if n == 4 and val == 1:
      roman = roman[:-1]+'IX' if last_digit=='V' else roman+'IV'
    elif n == 4 and val == 10:
      roman = roman[:-1]+'XC' if last_digit=='L' else roman+'XL'
    elif n == 4 and val == 100:
      roman = roman[:-1]+'CM' if last_digit=='D' else roman+'CD'
    else:
      roman += dict[val]*n
  return roman

if __name__ == "__main__":
  input_number = 3
  print(num_conversion(input_number))




