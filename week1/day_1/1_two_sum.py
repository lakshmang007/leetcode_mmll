"""
Problem: Two Sum
LeetCode #: 1
Concept: Hash Map
Time Complexity: O(n)
Space Complexity: O(n)
Date: 2026-02-23
"""

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i