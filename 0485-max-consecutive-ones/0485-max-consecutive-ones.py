""" kadne algo 
when 1 increse count and maxcount  (max)
when 0 count =0 nothing to update to maxcount 
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count=0
        max_count=0
        
        for num in nums:
            if num ==1:
                count+=1
                max_count=max(max_count,count)
            else:
                count=0
        return max_count


