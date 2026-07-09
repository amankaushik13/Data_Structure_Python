'''Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_count=0
        count=0
        for i in range(0, len(nums)):
            num=nums[i]
            count=1
        
            while num+1 in nums:
                count+=1
                num+=1
            max_count=max(count,max_count)
        return max_count


'''
Time complexity: O(n^2)
Space complexity: O(1)'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        count = 1
        longest = 1
        previous_smaller = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num == previous_smaller:
                continue                  # Duplicate

            elif num == previous_smaller + 1:
                count += 1               

            else:
                count = 1               

            previous_smaller = num
            longest = max(longest, count)

        return longest
    
    '''
    Time complexity: O(nlogn)
    Space complexity: O(1)
    '''
