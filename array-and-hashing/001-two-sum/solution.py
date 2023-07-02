class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = dict()
        for index, value in enumerate(numbers):
            if value in visited:
                return [visited[value], index]
            visited[target - value] = index
        return []
