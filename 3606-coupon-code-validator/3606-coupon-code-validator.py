class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # ascii_ranges = [range(48, 58), range(65, 91), [95], range(97, 123)]
        businesses = {"electronics", "grocery", "pharmacy", "restaurant"}
        valid_codes = defaultdict(list)
        results = []

        # for the index in the range of len of list
        for idx in range(len(code)):
        #     if is active is true and business in list of businesses and string code not empty
            stripped_word = code[idx].replace("_", "")
            if isActive[idx] and businessLine[idx] in businesses and (stripped_word.isalnum() or (len(set(code[idx])) == 1 and "_" in set(code[idx]))):
                valid_codes[businessLine[idx]].append(code[idx])

        # once done with the loop sort the dictionary keys.  then get the values and sort those? LOL
        sorted_dict = dict(sorted(valid_codes.items()))

        for value in sorted_dict.values():
            results += sorted(value)

        return results