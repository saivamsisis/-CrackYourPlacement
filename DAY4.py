#To Day I have worked on strings
#1)Print all the duplicate characters in a string
def duplicate(s):
    count={}
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for stng,value in count.items():
        if value>1:
            print(stng," count:",value)
duplicate("sai vamsi")
#2)Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
            stack=[]
            map={"(":")","{":"}","[":"]"}
            for i in s:
                if i in map.keys():
                    stack.append(i)
                elif i in map.values():
                    if not stack or map[stack.pop()]!=i:
                        return False
            return not stack
#3) Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            if needle in haystack:
                l=[haystack]
                for i in range(len(haystack)):
                    if haystack[i:i+len(needle)]==needle:
                        return i
            else:
                    return -1
#4)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1=nums1[:m]
        l2=nums2[:n]
        res=l1+l2
        res.sort()
        for i in range(len(res)):
            nums1[i]=res[i]
        
    
        

        
           

                

            

            
                
        

         
        
        
