Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
Sample Input -> Output
rotate2('Hello') → 'lloHe'
rotate2('java') → 'vaja'

*********************
def rotate2(str):
  n = len(str)
  str = str[2:n] + str[:2]
  return str

str = input()
print(rotate2(str))
