class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
           seen = {}

           for current_index, current_number in enumerate(nums):
            complement = target - current_number
            if complement in seen:
                return [seen[complement],current_index]
            seen[current_number] = current_index