Write a  program to find maximum of each column of  2d array 
Sample Input -> Output
max_col([[1, 5, 13], [11], [9, 18]]) → [11, 18, 13] 
max_col([[1, 8, 1], [1,21], [9]]) → [9, 21, 1]

*********************

import itertools 

def max_col(input_list):
  res = [max(i) for i in itertools.zip_longest(*input_list, fillvalue = 0)]
  #zip_longest iterates the columns of  uneven length and fill the not lnown values with 0
  return res
if __name__ == "__main__":
  input_list = [[1, 8, 1], [1,21], [9]]
  print(max_col(input_list))
