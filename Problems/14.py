#Longest Common Prefix
#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
    
     
        prefix = strs[0]
        
        
        for i in range(1, len(strs)):
            remaining = ""
            
            for j in range(len(prefix)):
               
                if j < len(strs[i]) and prefix[j] == strs[i][j]:
                    remaining += prefix[j]
                else:
                    break
      
            prefix = remaining
