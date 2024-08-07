#1)Palindrome Linked List
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_vals = []
        while head:
            list_vals.append(head.val)
            head = head.next
        
        left, right = 0, len(list_vals) - 1
        while left < right and list_vals[left] == list_vals[right]:
            left += 1
            right -= 1
        return left >= right

#2)Delete nodes having greater value on right

class Solution:
    def compute(self,head):
        node = None
        if(head != None):
            while(head != None):
                temp = head
                head = head.next
                temp.next = node
                node = temp
   
            temp = node.next
            prev = node
            while(temp != None):
                if(prev.data > temp.data):
                    prev.next = temp.next
                    temp = temp.next
                else:
                    prev = prev.next
                    temp = temp.next
                
            while(node != None):
                temp = node
                node = node.next
                temp.next = head
                head = temp
                
        else:
            return None
            
        return head
