class Solution:
    
    def solve(self, s, left, right):
        if left >= right:
            return
        
        s[left], s[right] = s[right], s[left]
        
        self.solve(s, left + 1, right - 1)
    
    def reverseString(self, s: List[str]) -> None:
        self.solve(s, 0, len(s) - 1)