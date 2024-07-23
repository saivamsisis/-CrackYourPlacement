#To day I have solved 3 problems from Mathematical part
1)Excel Sheet Column Title
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=''
        while columnNumber>0:
            off=(columnNumber-1)%26
            res+=chr(ord('A')+off)
            columnNumber=(columnNumber-1)//26
        return res[::-1]
2) Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)
        print(x)
        y=int(b,2)
        print(y)
        s=x+y
        return bin(s)[2:]
        
3)Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        P=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            P[i]=prefix
            prefix=prefix*nums[i]
        
        post=1
        for i in range(len(nums)-1,-1,-1):
            P[i]=P[i]*post
            post=post*nums[i]
        return P
