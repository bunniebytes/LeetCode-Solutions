class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        _sum = 0
        subsets = self.get_subsets(nums)
        for subset in subsets:
            temp_XOR = 0
            for x in subset:
                temp_XOR ^= x
            _sum += temp_XOR

        return _sum


    def get_subsets(self, input_list):
        if not input_list:
            return [[]]
        first_element = input_list[0]
        rest_elements = input_list[1:]

        subsets_without_first = self.get_subsets(rest_elements)
        subsets_with_first = [[first_element] + subset for subset in subsets_without_first]

        return subsets_with_first + subsets_without_first

        

            