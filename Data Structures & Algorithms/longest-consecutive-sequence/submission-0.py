class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest_streak = 0
        for current_num in hash_set:
            if current_num-1 not in hash_set:
                current_streak = 1
                while current_num + 1 in hash_set:
                    current_num += 1
                    current_streak += 1
            
                longest_streak = max(longest_streak,current_streak)
        return longest_streak