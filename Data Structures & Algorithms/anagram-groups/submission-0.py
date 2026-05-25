class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        from collections import defaultdict
        temp_dict = defaultdict(list)
        for word in strs:
            char_counts = [0] * 26
            for c in word:
                char_counts[ord(c) - ord('a')] += 1
            
            temp_dict[tuple(char_counts)].append(word)
        
        return list(temp_dict.values())
            
