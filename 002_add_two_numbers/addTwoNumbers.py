# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = current = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1 = l1.next
            if l2:
                carry+=l2.val
                l2 = l2.next
            carry,val = divmod(carry,10)
            current.next =ListNode(val)
            current = current.next
            #current.next = current = ListNode(val)
        return head.next
if __name__ =='__main__':
    l1 = ListNode(2)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    s = Solution()
    r = s.addTwoNumbers(l1,l2)
    if r:
        print (str(r.val)+" "+str(r.next.val))
    else:
        print ('wss')
