'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

'''

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        for _ in range(k): # O(k)
            last = nums.pop()      # Remove last element O(1)
            nums.insert(0, last)   # Insert at the beginning O(n)

#Time Complexity: O(kn)
#Space Complexity: O(1)