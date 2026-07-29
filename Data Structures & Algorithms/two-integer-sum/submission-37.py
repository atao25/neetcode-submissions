class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # return i and j st the sum of the values = target

        # 1. brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # return []

        # 2. hash map
        # create map of num and target - num
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i  #num = key, indices = value
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        
        return []

