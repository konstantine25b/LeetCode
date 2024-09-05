#Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their 
# intersection
# . Each element in the result must be unique and you may return the result in any order.

class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))