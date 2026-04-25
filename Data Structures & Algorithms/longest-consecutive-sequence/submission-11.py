class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for nums in s:
            if nums - 1 not in s:
                length = 1 
                next_num = nums + 1 
                while next_num in s:
                    length += 1 
                    next_num += 1
                longest = max(longest,length)
        return longest
