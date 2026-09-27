# array of int nums 
# target 
# return the indices i , j so that target matches sum and i != j

# ask if the array is sorted? 
# ask if negative values are allowed??

# approach 1- brute force- iterate the array nested fix one index and then find the other index that can lead to target sum -> O(n^2)
# approach 2 - 2 pointer approach - if not sorted then sort first
# if sorted then initialize two indices left and right and then run a while loop until left < right ...and compare the sum of those to target ..if current sum is less than target then we need to increase left coz moving right would reduce -> O(nlogn) non sorted or (n) if sorted

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []

        A = []
        for index, num in enumerate(nums):
            A.append([num, index])
        
        A.sort()

        left = 0
        right = len(nums) -1
        while left < right:
            current_sum = A[left][0] + A[right][0]
            if current_sum == target:
                if A[left][1] < A[right][1]:
                    return [A[left][1], A[right][1]]
                else:
                    return [A[right][1], A[left][1]]
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -=1

        # if doesn't exist
        return []