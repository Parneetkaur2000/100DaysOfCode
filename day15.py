Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists, and should also be 
sorted.For example, given the following linked lists :
5 -> 8 -> 20 
4 -> 11 -> 15
The merged list should be :
4 -> 5 -> 8 -> 11 -> 15 -> 20

***********************
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoLinkedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      temp = ListNode
      if l1 is None:
        return l2
      if l2 is None:
        return l1
        
      if l1.val < l2.val:
        temp = l1
        l1.next = self.addTwoLinkedLists(l1.next, l2)
      else:
        temp = l2
        l2.next = self.addTwoLinkedLists(l2.next, l1)
            
      return temp
