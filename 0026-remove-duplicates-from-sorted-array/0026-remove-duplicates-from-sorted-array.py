#in-place doesn't create an extra space
"""i=0
j=1    swap 
pass 1
1,2,1
  i j




"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i+=1
            nums[i],nums[j]= nums[j],nums[i]  #swap 
        return i+1
        