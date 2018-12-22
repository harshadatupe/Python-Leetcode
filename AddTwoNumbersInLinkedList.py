# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = l1
        val2 = l2
        head=None
        last=None
        if val1==None:
            return l2
        elif val2==None:
            return l1
        
        carry=0
        while (val1 is not None and val2 is not None):
            temp=ListNode(None)
            var=val1.val+val2.val+carry
            sum=var%10
            carry=var/10
            temp.val=sum
            if head==None:
                head=temp
                last=temp
            else:
                last.next=temp
                last=temp
            val1=val1.next
            val2=val2.next
        while (val1!=None):
            temp=ListNode(None)
            var=val1.val+carry
            sum=var%10
            carry=var/10
            temp.val=sum
            last.next=temp
            last=temp
            val1=val1.next
        while (val2!=None):
            temp=ListNode(None)
            var=val2.val+carry
            sum=var%10
            carry=var/10
            temp.val=sum
            last.next=temp
            last=temp
            val2=val2.next
        if carry!=0:
            temp=ListNode(carry)
            last.next=temp
            last=temp
        return head
