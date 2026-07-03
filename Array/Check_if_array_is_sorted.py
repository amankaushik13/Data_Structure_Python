"""Given an array nums, return true if the array was originally sorted in non-decreasing order
"""

class is_sorted():
    def check(self, nums: list[int]) -> bool:
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
                
        return True
    

# Time Complexity: O(n)
# space complexity: O(1)
