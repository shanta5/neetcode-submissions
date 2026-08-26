class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]==nums[j]):
                    flag = 1
                else:
                    continue
        return bool(flag ==1)