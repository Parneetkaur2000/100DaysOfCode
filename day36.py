Given a set of characters generate all possible passwords from them. This means we should generate all possible permutations of words using the given characters, 
with repetitions and also upto a given length.
Examples:
Input : hack_it({a, b},2)
Output :
['a', 'b', 'aa', 'ab', 'ba', 'bb']

************************************

from itertools import product
def hack_it(chars,length):
  res = []
  for i in range(length):
    for j in product(chars,repeat = (i+1)):
      res.append(''.join(j))
  return res
      
  
if __name__ == "__main__":
  chars = ['a',"b"] 
  print(hack_it(chars,len(chars)))


