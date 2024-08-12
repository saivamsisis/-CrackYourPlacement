#)Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/')
        for dir in directories:
            if dir == '.' or not dir:
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return '/' + '/'.join(stack)

  #) Generate Parentheses
  class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openP, closeP, s):
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)
                return
            
            if openP < n:
                dfs(openP + 1, closeP, s + "(")
            
            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")

        return res
