Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.
Example 1:
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"

Example 2:
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"

***************************************************

from itertools import zip_longest
def return_vertically(input_string):
  return ["".join(x).rstrip() for x in zip_longest(*input_string.split(), fillvalue=" ")]
if __name__ == "__main__":
  input_string = "HOW ARE YOU"
  print(return_vertically(input_string))

