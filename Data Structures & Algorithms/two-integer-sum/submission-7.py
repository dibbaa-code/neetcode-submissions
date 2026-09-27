# array of int nums 
# target 
# return the indices i , j so that target matches sum and i != j

# ask if the array is sorted? 
# ask if negative values are allowed??

# approach 1- brute force- iterate the array nested fix one index and then find the other index that can lead to target sum -> O(n^2)
# approach 2 - 2 pointer approach - if not sorted then sort first
# if sorted then initialize two indices left and right and then run a while loop until left < right ...and compare the sum of those to target ..if current sum is less than target then we need to increase left coz moving right would reduce -> O(nlogn) non sorted or (n) if sorted

# approach 3 - iterate and create hashmap to store the value and index of each item and then another iteration to check if the complement of the item exist in the map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []
        
        itemValueToIndexMap = {}
        for index, num in enumerate(nums):
            complementNum = target - num
            if complementNum in itemValueToIndexMap:
                complementIndex = itemValueToIndexMap[complementNum]
                return [min(index, complementIndex), max(index, complementIndex)]
            
            itemValueToIndexMap[num] = index
        
        return []
            
