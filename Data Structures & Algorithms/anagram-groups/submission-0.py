class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            sorted_key = "".join(sorted(word))
            if sorted_key in anagram_map:
                anagram_map[sorted_key].append(word)
            else:
                anagram_map[sorted_key] = [word]

            
        return list(anagram_map.values())