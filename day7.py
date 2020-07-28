Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.An array is said to be monotonic if 
its elements, from left to right, are entirely non-increasing or entirely non -decreasing.

Sample Input:
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output:
True
*************

def monoArray(array):
  array1 =  sorted(array)
  array2 = sorted(array , reverse=True)
  if array == array1:
    return True
  elif array == array2:
    return True
  else:
    return False


if __name__ == "__main__":
  array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
  print(monoArray(array))
