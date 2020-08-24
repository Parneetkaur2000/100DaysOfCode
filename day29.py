Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:
Will share image in whatsapp group

Note:
The total number of elements of the given matrix will not exceed 10,000.

******************************************************************************

def return_diag(input_matrix):
 if not input_matrix: return []
 temp = []
 for i in range(len(input_matrix)):
   for j in range(len(input_matrix[0])):
     if len(temp)-1<i+j: temp.append([input_matrix[i][j]])
     else: temp[i+j].append(input_matrix[i][j])
 res,i = [],0
 for item in temp:
   if i%2==0: res += item[::-1]
   else: res += item
   i += 1
 return res
if __name__ == "__main__":
  input_matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
  ]
  print(return_diag(input_matrix))

