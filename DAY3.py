#CrackYourPlacement
'''TO DAY I HAVE DONE TWO QUESTIONS FROM ARRAYS:
WHICH ARE:
1)REMOVE DUPLICATES PROBLEM:'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        y=nums[0]
        l=[y]
        for i in nums:
            if i!=y:
                y=i
                l.append(i)
        for i in range(len(l)):
            nums[i]=l[i]
        
        return len(nums[:len(l)])
#2)MOVE ZEROS:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        l=[]
        for i in nums:
            if i!=0:
                l.append(i)
            else:
                c=c+1
        for i in range(c):
            l.append(0)
        for i in range(len(nums)):
            nums[i]=l[i]


            
        `
