Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


*************************************

def dfs(i, j, input_matrix):
  if i<0 or i>=len(input_matrix) or j<0 or j>=len(input_matrix[0]) or input_matrix[i][j]!='1':
      return
  input_matrix[i][j] ="-1"
  dfs(i - 1, j, input_matrix)
  dfs(i + 1, j, input_matrix)
  dfs(i, j - 1, input_matrix)
  dfs(i, j + 1, input_matrix)
def count_island(input_matrix):
  island_count = 0
  for i, _ in enumerate(input_matrix):
    for j, _ in enumerate(input_matrix[i]):
      if input_matrix[i][j] == '1':
        dfs(i, j, input_matrix)
        island_count += 1
  return island_count
if __name__ == "__main__":
  input_matrix = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
  ]
  print(count_island(input_matrix))

