Given two strings s and t , write a function to determine if t is an anagram of s.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False

*********************************

def check_anagram(sentence_1,sentence_2):
  sentence_1 = sentence_1.lower().replace(" ","")
  sentence_2 = sentence_2.lower().replace(" ","")
  if sorted(sentence_1)==sorted(sentence_2):
    return True
  else:
    return False
if __name__ == "__main__":
  sentence_1 = ""
  sentence_2 = ""
  print(check_anagram(sentence_1,sentence_2))

