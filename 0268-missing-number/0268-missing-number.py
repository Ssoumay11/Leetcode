"""
app1 brute check num form 0 to n and see whether it exist in the array o(n2)
app2  sum formula o(n)
app3 xor a^a=0
        a^0=a
index   missing^=i^num
i=0  num=3    cal  3^0^3   missing =0
i=1  num=0    cal  0^1^0   missing =1
i=2  num=1    cal  1^2^1   missing =2




"""
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing =len(nums)

        for i ,num in enumerate(nums):
            missing^=i^num           
        return missing

        


       
        