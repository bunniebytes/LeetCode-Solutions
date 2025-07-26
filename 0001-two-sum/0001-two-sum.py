class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {num : i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            needed_num = target - num
            needed_i = hash_map.get(needed_num)
            if needed_i and needed_i != i:
                return (i, needed_i)
        

                
                
