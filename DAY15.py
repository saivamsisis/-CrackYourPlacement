#to day i have solved this
#1)jump a game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target_num_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if target_num_index <= i + nums[i]:
                target_num_index = i
        return target_num_index == 0
        
