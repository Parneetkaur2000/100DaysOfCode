Given 2 sets of integers,  M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  
M or N  but do not exist in both.

Input Format
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format
Output the symmetric difference integers in ascending order, one per line.

Sample Input
4
2 4 5 9
4
2 4 11 12
Sample Output
5
9
11
12

***************************

len1 = int(input())
nums1 = sorted(list(map(int, input().split())))
len2 = int(input())
nums2 = sorted(list(map(int, input().split())))

p1 = 0
p2 = 0

while p1<len1 and p2<len2:
  if nums1[p1]>nums2[p2]:
    print(nums2[p2])
    p2+=1 
  elif nums1[p1]<nums2[p2]:
    print(nums1[p1])
    p1+=1
  else:
    p1+=1 
    p2+=1 
while p1<len1:
  print(nums1[p1])
  p1+=1
while p2<len2:
  print(nums2[p2])
  p2+=1
