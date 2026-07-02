'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
'''


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
       
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i=i+1
                nums[i]=nums[j]
        return i+1
           
#time Complexity: O(n)
#space Complexity: O(1)
