class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)
        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                old_index = stack.pop()[0]
                distance = index - old_index
                results[old_index] = distance
            stack.append((index, temperature))

        return results
