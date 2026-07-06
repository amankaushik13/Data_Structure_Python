class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        prev = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                result += 1
            else:
                if prev < result:
                    prev = result
                result = 0

        return max(result, prev)
    

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''