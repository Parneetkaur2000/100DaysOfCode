Given an array arr[] with N elements, the task is to find out the longest sub-array which has the shape of a mountain.The Longest Peak consists of elements 
that are initially in ascending order until a peak element is reached and beyond the peak element all other elements of the sub-array are in decreasing order.

Input: arr = [2, 2, 2] 
Output: 0 
Explanation: 
No sub-array exists that shows the behaviour of a mountain sub-array.

Input: arr = [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5] 
Output: 11 

**************************

def LongestPeak(a):
  result=0
  count  = 0
  if len(a) < 0:
      result = 0
  if  len(a)==3:
      for i in range(1,len(a)-1):
          if a[i] > a[i-1] and a[i] > a[i+1]:
              result = 3
  else:
      for i in range(1,len(a)-1):
          if a[i] > a[i-1] and a[i] < a[i+1]:
              count += 1
          elif a[i] > a[i+1]:
              count +=1
          elif a[i-1]>a[i] and a[i+1]>a[i]:
              if count > result:
                  result = count+1
              count = 1
      if count > result:
          result = count+1
  return result



if __name__ == "__main__":
  d = [ 1, 3, 1, 4, 5, 6,
        7, 8, 9, 8, 7, 6, 5 ]
  print(LongestPeak(d))
