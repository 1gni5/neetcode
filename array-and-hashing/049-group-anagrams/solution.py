from collections import defaultdict

class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for word in words:
            count = [0] * 26
            for character in word:
                count[ord(character) - ord('a')] += 1
            results[tuple(count)].append(word)
        return results.values()
