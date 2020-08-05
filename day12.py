You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single 
digit. Add the two numbers and return it as a linked list.You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Sample input
(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)

Sample output
7 -> 8 -> 0 -> 7

***************

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next
        
class Linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0
    def append_item(self, val):
      self.node = ListNode(val)

      if self.head is None:       
        self.head = node
        self.count += 1
        return

      else:
        self.pre = self.head
        while(pre.next != None):
          pre = pre.next

        self.pre.next = self.node
        self.tail = self.node
        self.count += 1

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = curr = ListNode()
        while l1 and l2:
            total = l1.val + l2.val + carry
            curr.next = ListNode(total % 10)
            carry = total//10
            l1, l2, curr = l1.next, l2.next, curr.next
        while l1:
            total = l1.val + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            l1, curr = l1.next, curr.next
        while l2:
            total = l2.val + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            l2, curr = l2.next, curr.next
        if carry>0:
            curr.next = ListNode(carry)
        return head.next
    
