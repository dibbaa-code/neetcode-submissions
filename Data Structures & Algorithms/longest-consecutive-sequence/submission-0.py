# array of integers nums, 
# return legth longest of consecutive sequence that can be formed
# consecutive sequence -> each element is ecact 1 greater than previous one
# [2,20,4,10,3,4,5] -> [2,3]

# approach 1 - sort it but O(nlogn)
# approach 2 - hashset (2, 20, 4, 10, 3, 4, 5) - current longest consecutive sequence -- for ith element check if x-1 is present 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)
        
        longestLength = 0
        for num in numSet:
            if num -1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longestLength = max(length, longestLength)
        
        return longestLength



        