# Sort an Array

# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
#ამ ამოცანაში ჩვენ დავსორტეთ O(n*2)-ში ამიტომ ტესტებში დორში ჩაიჭრება


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)  
        
        for i in range(n):
            for j in range(i,n):
                if nums[i]>nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums 