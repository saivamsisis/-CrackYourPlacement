#CrackYourPlacement
'class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        y=nums[0]
        l=[y]
        for i in nums:
            if i!=y:
                y=i
                l.append(i)
        for i in range(len(l)):
            nums[i]=l[i]
        
        return len(nums[:len(l)])'
            
        `
