#CrackYourPlacement
'''I HAVE STARTED THE ARSHs 45 DAYS CHALLENGE WHERE ON DAY I HAVE COMPLETED ONLY 1 PROBLEM BUT LEARNED  LOT OF BASICS CONCEPTS.
I HAVE COMPLETED MAXIMUM PRODUCT OF THREE NUMBERS PROBLEM FROM LEET CODE.
HERE IS THE CODE I HAVE DONE.'''

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        pro=max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
        return pro
        
        
