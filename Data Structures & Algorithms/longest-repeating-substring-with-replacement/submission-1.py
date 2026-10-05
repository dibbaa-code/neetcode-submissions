# given string s only uppercase english characters 
# K choose upto k chars of sting with any other char
# after doing at most k replacement return the longest substring that contains only 1 distinct char

# XYYX  -> XYXX

#AAABABA
class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        if (len(s) < 2):
            return len(s)

        l = 0
        maxf = 0
        count = {}
        longestlength = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf  > k:
                count[s[l]] -= 1
                l +=1

            longestlength = max(longestlength, r-l+1)
        
        return longestlength

            



        
        