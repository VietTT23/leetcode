"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
"""
LINK:
https://pythontutor.com/render.html#code=nums%20%3D%20%5B2,7,11,15%5D%0Atarget%20%3D%209%0A%0Afor%20i%20in%20range%28len%28nums%29%29%3A%0A%20%20%20%20for%20j%20in%20range%28i%2B1,%20len%28nums%29%29%3A%0A%20%20%20%20%20%20%20%20_nums_i%20%3D%20nums%5Bi%5D%0A%20%20%20%20%20%20%20%20_nums_j%20%3D%20nums%5Bj%5D%0A%20%20%20%20%20%20%20%20if%20target%20-%20nums%5Bi%5D%20%3D%3D%20nums%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20val%20%3D%20%5Bnums%5Bi%5D,%20nums%5Bj%5D%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20tS%20%3D%20%5Bi,j%5D&cumulative=false&curInstr=37&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
"""

# CODE IN LEETCODE
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i,j]
"""

# CODE TEST
nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if target - nums[i] == nums[j]:
            twoSum = [i, j]
            print(twoSum)

