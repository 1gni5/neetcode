class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for x in nums:
            if (x - 1) not in num_set:
                length = 1
                while (x + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
