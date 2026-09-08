# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        i_p = 1
        j_p = 1
        i_arr = []
        j_arr = []
        while i < len(nums) and j >= 0:
            i_p *= nums[i]
            j_p *= nums[j]
            i += 1
            j -= 1
            i_arr.append(i_p)
            j_arr.append(j_p)
        a = i_arr
        b = j_arr[::-1]
        ans = []
        ans.append(b[1])
        for i in range(1, len(a) - 1):
            ans.append(a[i - 1] * b[i + 1])
        ans.append(a[len(a) - 2])
        return ans
