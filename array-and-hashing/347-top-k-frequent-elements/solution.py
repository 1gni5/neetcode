from collections import Counter

class Solution:
    def topKFrequent(self, numbers: List[int], k: int) -> List[int]:
        frequency = [[] for x in range(len(numbers) + 1)]
        counts = Counter(numbers)

        for number, count in counts.items():
            frequency[count].append(number)

        results = []
        for index in range(len(numbers), 0, -1):
            for x in frequency[index]:
                results.append(x)
                if len(results) == k:
                    return results

