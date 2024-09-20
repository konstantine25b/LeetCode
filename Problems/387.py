# 387. First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_map={}

        for char in s:
          if char in count_map:
              count_map[char]+=1
          else:
              count_map[char]=1
        for i, char in enumerate(s):
            if count_map[char]==1:
                return i
        return -1