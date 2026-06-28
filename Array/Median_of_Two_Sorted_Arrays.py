'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
 
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.'''



class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums=sorted(nums1+nums2)
        if len(nums)%2==1:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2
        

#Time Complexity = O((m+n) log(m+n)) 

'''
O(m+n) for nums1+nums2
O(log (m+n)) for sorting
'''
#Space Complexity = O(m+n) 