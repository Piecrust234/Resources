class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsToArray = {} # Hashmap/Dict containing complements

        for i in range(len(nums)):
            if (target - nums[i]) in numsToArray: # see if the complement to the current element of the nums List is in the hashmap (target - nums[i] is the complement)
                return [i,numsToArray[target - nums[i]]] # return the indices of the two complements. 1) the current index 2) the index of the complement already in the map
            numsToArray[nums[i]] = i # if the complement is not in the dict/map, then add the v: i  