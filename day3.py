Smallest Difference   
Write a function that takes in two non-empty arrays of integers, find the pair of numbers (one from each array) whose absolute difference is closet to zero, and returns an array containing these two numbers, with the numbsers, with the number from the first array in the first position.

You can assume that there will only be one pair of numbers with the smallest difference.

Sample Input

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

Sample Output

[28, 26]

Optimal Solution
O(nlog(n)) + O(mlog(m) + O(m+n))
where,
n is the size of arrayOne
m is the size of arrayTwo

*******************
import math
def smallestDifference(arrayOne, arrayTwo):
  arrayOne.sort()
  arrayTwo.sort()
  i = 0
  j = 0
  list = []
  s = math.inf #Constant positive floating infinity value
  while(i<len(arrayOne) and j<len(arrayTwo)):
    n1 = arrayOne[i]
    n2 = arrayTwo[j]
    
    if n1 > n2:
      r = n1 - n2
      j+= 1
    elif n2 > n1:
      r = n2 - n1
      i+= 1
    else:
      return [n1,n2]
    
    if r < s:
      s = r
      list = [n1,n2]
  return list


if __name__ == "__main__":
  arrayOne = [-1, 5, 10, 20, 28, 3]
  arrayTwo = [26, 134, 135, 15, 17]
  print(smallestDifference(arrayOne, arrayTwo))
