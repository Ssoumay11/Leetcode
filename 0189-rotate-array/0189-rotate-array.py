"""
array have two indexing 
1. pos index 
2.  neg index
[1,2,3,4,5,6,7] k=3 
5,6,7,1,2,3,4

rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
  we split the array like arr=[1,2,3,4,5,6,7]  arr[3]=4
  but if we do arr[1:3] =2,3

nums[start : end : step ]
"""
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] +  nums[:-k]

        