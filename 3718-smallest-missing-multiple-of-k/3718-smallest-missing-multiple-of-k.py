
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Convert list to set for O(1) lookups
        num_set = set(nums)
        multiple = k
        
        # Check multiples of k sequentially
        while multiple in num_set:
            multiple += k
            
        return multiple