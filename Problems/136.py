#Single Number

#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique_numbers = set()

        for num in nums:
            if num in unique_numbers:
                unique_numbers.remove(num)

            else:
                unique_numbers.add(num)

        return unique_numbers.pop()


        
        