#take the number check for other number whose both sum is equal to target
#[2,7,11,15]  target 9 first element is 2  find that number that target - elements
#9-2 we have to find 7 using map 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i, num in enumerate(nums):
            complement=target-num

            if complement in seen:
                return [seen[complement],i]  #checking into map for 7, 2 
            seen[num]=i  
        