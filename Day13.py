#to day i Have solved following problems:
#1)Convert Binary Number in a Linked List to Integer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def toList(head, l) :
            if head :
                l.append(head.val)
                if head.next :
                    toList(head.next, l)
                return l
            return []
        l = toList(head, [])
        n2 = sum([l[len(l) - i - 1] * 2 ** i for i in range(len(l))])
        return n2
#2)Subarray Sum Equals K
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 and count 1
        
        for num in nums:
            prefix_sum += num  # Update the running prefix sum
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]  # Increment count if (prefix_sum - k) is found
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1  # Update the frequency of the current prefix sum
            else:
                prefix_sum_count[prefix_sum] = 1  # Initialize the frequency if the prefix sum is seen for the first time
        
        return count
