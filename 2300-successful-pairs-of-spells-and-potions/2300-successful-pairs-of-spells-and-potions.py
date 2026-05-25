class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        len_potions = len(potions)
        for idx, spell in enumerate(spells):
            left = 0
            right = len_potions - 1
            # if spell * potions[left] >= success:
            #     result[idx] = len(potions)
            #     continue
            # if spell * potions[right] < success:
            #     continue
            while left <= right:
                mid = (right + left) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            if spell * potions[mid] >= success:
                result.append(len_potions - mid)
            else:
                result.append(len_potions - right - 1)

        return result

        # loop through spells
        # for spell in spells:
        #     successful = 0
        #     loop through potions
        #     for potion in potions:
        #         if spell * potion >= success:
        #             successful += 1
        #     result.append(successful)
