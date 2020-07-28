Four Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all quadruplets in the array that sum up to the largest sum and return a two dimensional array of all these
quadruplets in no particular order.

************
def fourNumberSum(array, targetSum):
    array.sort()
    dict ={}
    n = len(array)
    for i in range(n-1):
        for j in range(i+1,n):
            value = targetSum - (array[i]+array[j])
            if value in dict:
                for pair in dict[value]:
                    x,y = pair
                    if(x!= i and x!=j) and (y!=i and y!=j):
                        print(array[i],array[j],array[x],array[y])
            dict.setdefault(array[i] + array[j],[]).append((i,j))



if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
