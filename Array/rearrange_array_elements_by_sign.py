'''
 Rearrange Array Elements by Sign
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 '''
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result=[0] * len (nums)
        pos=0
        neg=1
        for num in nums:
            if num > 0:
                result[pos]=num
                pos+=2
            else:
                result[neg]=num
                neg+=2
        
        return result


'''
Time complexity: O(n)
Space complexity: O(n)

'''