# nums, 
# return all triplets where their sum is 0 

# approach 1 - sort and fix 1 and then two pointer for the next 2  - O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        numsSorted = sorted(nums)

        for index, num in enumerate(numsSorted):
            if index > 0 and num == numsSorted[index - 1]:
                continue

            target = -num
            left = index+1
            right = len(numsSorted)-1

            while left < right:
                if numsSorted[left] + numsSorted[right] == target:
                    triplets.append([numsSorted[index], numsSorted[left], numsSorted[right]])
                    left += 1
                    right -= 1
                    while left < right and numsSorted[left] == numsSorted[left - 1]:
                        left += 1
                    while left < right and numsSorted[right] == numsSorted[right + 1]:
                        right -= 1
                elif numsSorted[left] + numsSorted[right] < target:
                    left +=1
                else:
                    right -=1
            
        return triplets
        