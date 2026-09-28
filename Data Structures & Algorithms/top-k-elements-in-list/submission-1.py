# integer array nums and integer k
# return most frequent elements  in the array 

# approach 1 hashmap - store num -> count, sort it  and then return the sliced array on k index --  O(nlogn)
# approach 2 map for num -> count and then (count, num) in min heap of size k --- O(nlogk)


# approach 3 buckets??
# hash map for num -> count - O(n)
# list of list --- frequency[i] is list of numbers that are i times in nums O(n)
# iterate from len(num)-1 to 0, return once the result len reach k O(n)
# O(n)



class Solution: # [7,7]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resultList = []
        numToCountMap = defaultdict(int) # 7 - 2
        for num in nums:
            numToCountMap[num] +=1
        
        countToNumListMap = defaultdict(list) # 2 - 7
        for num in numToCountMap:
            count = numToCountMap[num]
            countToNumListMap[count].append(num)
        

        for index in range(len(nums), -1, -1): 
            if countToNumListMap[index]:
                resultList.extend(countToNumListMap[index])

            if len(resultList) == k:
                break
        
        return resultList