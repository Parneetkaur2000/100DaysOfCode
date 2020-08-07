Given a linked list, remove the n-th node from the end of the list and return its head.
Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

************************

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      node = head
      c = 0
      while node:
        node = node.next
        c += 1
      if c == n:
        return head.next
      node = head
      for _ in range(0,c-n-1):
        node = node.next
      if node.next.next:
        node.next = node.next.next
      else:
        node.next = None
      return head
      
