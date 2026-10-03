# string s, 
# return the length of the longest substring without duplicate chars

# approach 1. - sliding window in hashmap char - index and and then check if the next char is in set if not then add ..if yes then drop the char in hashmap until that index and then add the new one and keep a current lenght and longest length variable 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) < 2):
            return len(s)
        
        longestlength = 0
        mapCharToIndex = {}
        slidingWindowStartIndex = 0
        slidingWindowEndIndex = 0
        for currIndex, char in enumerate(s):
            if char in mapCharToIndex and mapCharToIndex[char] >= slidingWindowStartIndex:
                existingCharIndex = mapCharToIndex[char]
                slidingWindowStartIndex = existingCharIndex + 1
            
            mapCharToIndex[char] = currIndex
            slidingWindowEndIndex = currIndex
            longestlength = max(longestlength, slidingWindowEndIndex-slidingWindowStartIndex+1)
 
        return longestlength
