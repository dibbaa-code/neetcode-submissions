# integer array 
# return true if ANY value is duplicated otherwise false

# approach 1 - go through the array iterate and store in a hashmap and check everytime before storing if the number exists in the hashmap then return true and break the loop if not got through the whole loop and return false
# approach 2 - instead of hashmap i can use hashset O(n) and space O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <2:
            return False

        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)
        
        return False