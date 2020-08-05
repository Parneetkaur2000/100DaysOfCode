Given a singly linked list of characters, write a function that returns True if the given list is a palindrome, else False.

Sample input
("r" -> "a" -> "d" -> "a" -> "r" )

Sample output
True

****************

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def checkPalindrome(self, l1: ListNode):
      m = l1
      n = l1
      while n and n.next:
        m = m.next
        n = n.next.next
        
      temp = m.next
      m.next = None
      
      while temp:
        next = temp.next
        temp.next = m
        m = temp
        temp = next
        
      while m and l1:
        if m.val != l1.val:
          return False
        m = m.next
        l1 = l1.next
      return True
        
      
    


    
    
    
    
    
