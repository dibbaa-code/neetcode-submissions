# two string s and t
# retrn true if s, t are anagrams of each other otherwise false
# anagrams -> same characters same no of times but order doesn't matter 

# approach 1 - iterate both strings one char at a time and store the count in 2 hashmaps and then check the length of both hashmaps if same then iterate one hashmap and check the other hashmap if same character exist in that one with same count
# runtime - O(n + m) , space O(n+ m)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) == 0 or len(t) == 0):
            return True

        charMapForS = {}
        for char in s:
            if char not in charMapForS:
                charMapForS[char] = 1
            else:
                charMapForS[char] += 1
        
        charMapForT = {}
        for char in t:
            if char not in charMapForT:
                charMapForT[char] = 1
            else:
                charMapForT[char] += 1
        
        if len(charMapForS) != len(charMapForT):
            return False
        
        for char in charMapForS:
            if char not in charMapForT:
                return False
            elif charMapForS[char] != charMapForT[char]:
                return False
        
        return True