Move Element to End

You're given an array of integers and an integer. Write a function that moves all instance of that integer in the array to the end of the array and returns the array.
Write a function that should perform this in place (i.e , it should mutate the input array) and doesn't need too maintain the order of the other integer.

Sample Input:
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample Output:
[1, 3, 4, 2, 2,2,2,2]

************
def moveElementToEnd(array, toMove):
  for ele in array:
        if ele == toMove:
            array.append(array.pop(array.index(ele)))
  return array


if __name__ == "__main__":
  array = [2, 1, 2, 2, 2, 3, 4, 2]
  toMove = 2
  print(moveElementToEnd(array, toMove))
