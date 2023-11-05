class Solution:
    def search(self, nums: List[int], target: int) -> int:
        R = len(nums) - 1 # get index of farthest right element
        L = 0 # Get index of farthest left element

        while L <= R: # While the left index is smaller than the right index
            m = round((L + R)/ 2) # find the current mid point.
            if nums[m] < target: # if the value at the current mid point is less than the target, the target must be to the right; update left point, and re-calc mid.
                L = m + 1 # left can be the previous midpoint now
            elif nums[m] > target: # if value at current midpoint greater than target, update right point to be midpoint-1, to work towards convergence
                R = m - 1
            else: # if current mid point is neither less than or greater than midpoint element, then midpoint element must be the target.
                return m # return the index of the midpoint
        return -1