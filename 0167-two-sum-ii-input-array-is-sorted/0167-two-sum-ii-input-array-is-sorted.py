"""
array is sorted 
numbers = [2,3,4], target = 5
left = 2 
right= 4
sum = 6  if sum is greater than the target we move right by -1"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0
        right=len(numbers)-1
        while left < right:
            total=numbers[left] + numbers[right]

            if total== target:
                return[left+1,right+1]
            elif total < target:
                left+=1
            else:
                right-=1
        