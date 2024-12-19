
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxlen=0
        for i in range(0,len(s)):
            arr=[]
            flag=0
            for m in (s[i::]):
                if(m in arr):
                    break
                else:
                    arr.append(m)
            lens=len(arr)
            if(maxlen<lens):
                maxlen=lens
        return maxlen