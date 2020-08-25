Write a Python program of recursion list sum.
Example 1:
Input: grid = [1, 2, [3,4],[5,6]]
Output: 21

************************
Solution 1 (Using recursion):

def recursive_sum(input_matrix):
  val = 0
  for i in input_matrix:
    if type(i) == type([]):
      val = val + recursive_sum(i)
    else:
      val = val+ i
  return val
      
if __name__ == "__main__":
  input_matrix = [1, 2, [3,4],[5,6]]
  print(recursive_sum(input_matrix))
  
********************************
Solution 2 (Using sum function):

def recursive_sum(input_matrix):
  for i in input_matrix :
    for j in i:
      s = sum(j)
  return s
 
if __name__ == "__main__":
   input_matrix = [1,2, [3,4],[5,6]]
   print(recursive_sum(input_matrix))
