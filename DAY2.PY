#CrackYourPlacement
'''TO DAY I HAVE DONE TWO PROBLEMS BUT ENJOYED A LOT DOING THE PROBLEMS.
TO DAY I HAVE DONE PROBLEMS FROM ARRAY TOPIC WHICH ARE:
1)TWO SUM
2)COLOR SORT
THOUGHT THEY ARE EASY QUESTION BUT WHILE SOLVING THESE QUESTION I GOT VERY GOOD REVISION ON SORTING ALGO
HERE IS MY CODE FOR THE PROBLEMS'''
#1)TWO SUM:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r=len(nums)
        
        for i in range(0,r-1):
            for j in range(i+1,r):
                if nums[i]+nums[j]==target:
                    return ([i,j])
#2)COLOR SORT:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left,right=0,len(nums)-1
        i=0
        def swap(i,j):
            nums[i],nums[j]=nums[j],nums[i]
        while i<=right:
            if nums[i]==0:
                swap(left,i)
                left+=1
            elif nums[i]==2:
                swap(i,right)
                right-=1
                i-=1
            i+=1
        return nums

                     

        
