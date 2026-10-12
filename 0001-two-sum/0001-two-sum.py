class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #brute 
        #two loop 
        #hold the first number in first loop then second no in second loop 
        n=len(nums)
        #range fuc (start , end , step (opt))
        for i in range(n): #first no 
            for j in range(i+1,n):#second no
                if nums[i]+nums[j]==target:
                    return[i,j]