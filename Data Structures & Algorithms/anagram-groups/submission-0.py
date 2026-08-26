class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in anagram_groups:
                anagram_groups[key] = []
                anagram_groups[key].append(word)
            else:
                anagram_groups[key].append(word)
        result = []
        for group in anagram_groups.values():
            result.append(group)
        return result                
        