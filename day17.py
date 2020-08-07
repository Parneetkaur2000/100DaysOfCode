Given a singly linked list and an integer K, reverses the nodes of the
list K at a time and returns modified linked list.
NOTE : The length of the list is divisible by K
Example :
Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

*********************

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapLinkedLists(self, l1: ListNode,key: int) -> ListNode:
      current = l1
      for i in range(key):
        if not current:
          return l1
        current = current.next
            
        # Basic Reverse in Linked List
      current = l1
      previous = None
      for i in range(key):
        current_next = current.next
        current.next = previous
        previous = current 
        current = current_next
        
        # A recursive call to carry on with it.
      l1.next = self.swapLinkedLists(current, key)
      return previous
