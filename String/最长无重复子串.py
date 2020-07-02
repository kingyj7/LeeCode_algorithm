#https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

#!/usr/bin/python
# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, fullstr) :
        maxLen = 0
        tmp_substr = []
        
        for s in fullstr:
            tmp_substr.append(s)
            
            if len(tmp_substr) == len(set(tmp_substr)):
                continue
            else:
                maxLen = len(tmp_substr)-1 if len(tmp_substr)-1 > maxLen else maxLen
                
                retain = [s]
                for i in range(1,len(tmp_substr)+1):
                    if tmp_substr[-1] != tmp_substr[-i-1]:
                        retain.append(tmp_substr[-i-1])
                    else:
                        break
                
                tmp_substr = retain
                
                
        maxLen = len(tmp_substr) if len(tmp_substr) > maxLen else maxLen
        
        return maxLen

if __name__ == '__main__':
    test = "pwwkewtasc"
    print(Solution().lengthOfLongestSubstring(test))
