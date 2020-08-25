This problem is about generating Power set in lexicographical order.
Examples :
Input : abc
Output : ["a","ab","abc","ac","b","bc","c"]

Input : "banana"
Output = ['a', 'aa', 'aaa', 'aaab', 'aaabn', 'aaabnn', 'aaan', 'aaann', 'aab', 'aabn', 'aabnn', 'aan', 'aann', 'ab', 'abn', 'abnn', 'an', 'ann', 'b', 'bn', 'bnn', 'n', 'nn']

************************************************

from itertools import combinations
def power_set(input_string):
  n = len(input_string)
  input_string = sorted(input_string)
  powerSet = set()
  
  for i in range(n):
    temp = combinations(input_string,i+1)
    powerSet = powerSet.union(set(map(''.join, temp)))
    
  powerSet = sorted(powerSet)
  return powerSet
if __name__ == "__main__":
  input_string = "abc"
  print(power_set(input_string))
