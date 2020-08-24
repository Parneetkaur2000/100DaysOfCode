You are given a binary tree in which each node contains an integer value.Find the number of paths that sum to a given value.The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
Example:
root = [10,5,-3,3,2,None,11,3,-2,None,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

***********************************************

class Solution:
    def rec_sum(self, node, cursum, target):
        if node == None:
            return
        cursum += node.val
        complement = cursum-target
        if complement in self.sum_dict:
            self.result += self.sum_dict[complement]
        if cursum in self.sum_dict:
            self.sum_dict[cursum]+=1
        else:
            self.sum_dict[cursum]=1
        self.rec_sum(node.left, cursum, target)
        self.rec_sum(node.right, cursum, target)
        self.sum_dict[cursum]-=1
    def pathSum(self, root, sum):
        if root==None:
            return 0
        
        self.sum_dict = {0:1}
        self.result = 0
        self.rec_sum(root, 0, sum)
        return self.result
        
## This class will be used from creating the nodes of tree
class newNode: 
    def __init__(self, val): 
        self.val = val  
        self.left = self.right = None
def sum_tree(input_matrix,sum_val):
  #write your code here
  #####
  #The function below creates the tree data structure from the given array
  #####
  root = None
  def insertLevelOrder(arr, root, i, n): 
    if i < n: 
      if arr[i]!=None:
        temp = newNode(arr[i])  
        root = temp  
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)  
        root.right = insertLevelOrder(arr, root.right,2 * i + 2, n) 
    return root 
  root = insertLevelOrder(input_matrix, root, 0, len(input_matrix))
  
  
 
  return Solution().pathSum(root, sum_val)
if __name__ == "__main__":
  input_matrix = [10,5,-3,3,2,None,11,3,-2,None,1]
  sum_val = 8
  print(sum_tree(input_matrix,sum_val))

