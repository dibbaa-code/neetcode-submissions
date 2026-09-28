# array of strings
# group all anagram into sublists

# approach 1 - bruteforce - fix one string in the array and then do nested loop to find its anagram in rest of the array 
# use hashmap to store char to count for the string

# approach 2 - sort the strings in place in the map and then just do a equal check
#[act,opst, opst, act, opst,atn ]

# approacvh 3 try to do it in one iteration instead of fixing 
# iterate through the array of strings and store the 
# map = {"act" - {a - 1, c-1, t -1}, "pots" - {p-1, o, t, s}, }

# approach map of array of 26 size a-z as key  and value as list of anagrams 




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCountArrayToAnagramsStrMap = defaultdict(list)
        for str in strs:
            charCountArray = [0] * 26
            for char in str:
                charCountArray[ord(char) - ord('a')] += 1
            
            charCountArrayToAnagramsStrMap[tuple(charCountArray)].append(str)
        
        return list(charCountArrayToAnagramsStrMap.values())        

        