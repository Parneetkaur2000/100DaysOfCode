Three Number Sum

Write a function that takes in a non empty array of distinct integers and an integer representing a target sum. The function should find a list of triplets in
the array that sum upto the target sum and return a two-dimensional array of all the these triplets.The numbers in each triplet should be order in ascending 
order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.If no three numbers sum up to the target sum, 
the function should return an empty array

*********
def threeNumberSum(array, targetSum):
    array.sort()
    n = len(array)
    list = []
    
    for i in range(n-2):
      m = array[i]
      start = i+1
      end = n-1
      s = targetSum - m
      while start<end:
        if s == array[start] + array[end]:
          list.append(sorted([m,array[start],array[end]]))
          start +=1
        elif s > array[start]+array[end]:
          start+=1
        else:
          end -= 1
    return list
        
        
      

    
if __name__ == '__main__':
  array =  [12, 2, 1, 3, -6, 5, -8, 6]
  targetSum = 0
  print(threeNumberSum(array, targetSum))
  
