class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groupnum = {}
        unique_nums = set(nums)
        for number in unique_nums:
            key = nums.count(number)
            if key not in groupnum:
                groupnum[key] = []
            groupnum[key].append(number)
        result = []
        sorted_freqs = sorted(groupnum.keys(), reverse=True)
        

        for freq in sorted_freqs:
            for num in groupnum[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
        