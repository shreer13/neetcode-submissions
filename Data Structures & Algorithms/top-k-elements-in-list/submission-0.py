class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_elem ={}
        for i in nums:
            if i in freq_elem:
                freq_elem[i] += 1
            else:
                freq_elem[i] = 1
        
        sorted_dict = dict(sorted(freq_elem.items(), key = lambda item:item[1], reverse = True))

        return list(sorted_dict.keys())[:k]