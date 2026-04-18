class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_nums = {}

        for i in range(len(nums)):
            if target - nums[i] in previous_nums:
                return  [previous_nums[target - nums[i]], i]

            previous_nums[nums[i]] = i

        return [-1, -1]
      
        