class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if 1 <= len(nums) <= 1000:
            for i in range(len(nums)):
                if 1 >= nums[i] and nums[i] >= 1000:
                    return " "
                else:  
                    return nums + nums