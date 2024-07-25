#Today i have solved following questions on arrays:
#1)Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        print(count)
        x= max(count.values())
        for key,val in count.items():
            if val==x:
                return key
                break
#2)Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        l=[]
        for key,val in count.items():
            if val==2:
                l.append(key)
        return l
#3)Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        area=1
        res=0
        while l<r:
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)
            if height[l]<height[r]:
                l=l+1
            elif height[l]>height[r]:
                r=r-1
            else:
                r=r-1
        print(res)
        
        
        return res
        
            
