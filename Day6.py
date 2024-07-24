#To day I have solved following problems:
#1)Find the Duplicate Number:
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i in count.keys():
                count[i]+=1
            else:
                count[i]=1
        max_key = max(count, key=count.get)
        return max_key
#2)Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipL,skipR=s[l+1:r+1],s[l:r]
                return (skipL==skipL[::-1] or skipR==skipR[::-1])
            l,r=l+1,r-1
        return True
#3)Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        ma=0
        while r<len(prices):
            if prices[l]<prices[r]:
                pro=prices[r]-prices[l]
                ma=max(ma,pro)
            else:
                l=r
            r+=1
        return ma
  #4)Permute two arrays such that sum of every pair is greater or equal to K
a = list(map(int,input().split()))
b = list(map(int,input().split()))
k = int(input())
n = len(a)
a.sort(reverse=True)

    b.sort()

    for i in range(n):
        if (a[i] + b[i] < k):
            print("Yes")

    print("No")

