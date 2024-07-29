#today i have solved following problems:
#1)122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        start = prices[0]
        len1 = len(prices)
        for i in range(0 , len1):
            if start < prices[i]: 
                max += prices[i] - start
            start = prices[i]
        return max
#2)Set Matrix Zeroes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rLen = len(matrix)
        cLen = len(matrix[0])
        rows = [False] * rLen
        cols = [False] * cLen
        for r in range(rLen):
            for c in range(cLen): # Traverse through matrix and save rows and cols that must be 0
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True
        for i, r in enumerate(rows): # iterate through rows that must be 0 and set to 0
            if r:
                for c in range(cLen):
                    matrix[i][c] = 0
        for j, c in enumerate(cols): # iterate through cols that must be 0 and set to 0
            if c:
                for r in range(rLen):
                    matrix[r][j] = 0
        

        
