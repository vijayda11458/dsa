class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =0
        mapData = set()
        max_length =0
        for right in range(len(s)):
            while s[right] in mapData:
                mapData.remove(s[left])
                left+=1
            mapData.add(s[right])
            max_length = max(right-left+1,max_length)
        return max_length