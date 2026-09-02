class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums[i+1:]:
                for j in range(len(nums)):
                    if a == nums[j] and j != i:
                        return [i,j]

        