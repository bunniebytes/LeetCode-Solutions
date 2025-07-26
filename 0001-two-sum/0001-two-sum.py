class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        i = 0
        for num in nums:
            hash_map[num] = i
            i += 1
        for i, num in enumerate(nums):
            needed_num = target - num
            needed_i = hash_map.get(needed_num)
            if needed_i and needed_i != i:
                return (i, needed_i)
        

                
                
