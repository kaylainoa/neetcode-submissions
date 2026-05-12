class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        notebook = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in notebook:
                return [notebook[diff], i]
            notebook[n] = i
        return
