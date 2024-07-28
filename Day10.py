#to day i have solved these problems
#1)All Unique Permutations of an array
#User function Template for python3
from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        answer=list(sorted(set(permutations(arr))))
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends

#2)Subarray Sums Divisible by K
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        fr = [0]*k
        fr[0]=1
        counter = 0
        ans = 0
        for num in nums:
            if num>=0:
                counter+=num
            else:
                counter+=(num%k)+k
            counter%=k

            ans += fr[counter]
            fr[counter]+=1
        
        return ans
