class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        set_nums = set(nums)
        for num in set_nums:
            if num-1 in set_nums:
                continue
            upper = num+1
            while upper in set_nums:
                upper += 1
            
            longest = max(longest, upper - num)
        
        return longest