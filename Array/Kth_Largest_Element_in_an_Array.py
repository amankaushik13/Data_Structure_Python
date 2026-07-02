"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""



import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        largest_k_elements=[]

       
        for i in range(k):  #Time complexity: O(k)

            heapq.heappush(largest_k_elements, nums[i]) #Time complexity: O(log k)
        
    
        for j in range(k,len(nums)):      #Time complexity: O(n-k)
            if largest_k_elements[0]< nums[j]:
                heapq.heappop(largest_k_elements) #Time complexity: O(log k)
                heapq.heappush(largest_k_elements,nums[j]) #Time complexity: O(log k)
        
        return largest_k_elements[0]
    

    '''
    total time complexity: O(k)  O(log k) +  O(n-k) O(2 log k)
    O(k log k) + O( n-k log k)
    O(n log k)

    Space Complexity: O(k)
    '''
