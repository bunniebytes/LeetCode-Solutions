class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        seen_flower = False # This lets us know if we don't add flower
        pot_counter = 0
        # loop through the flower bed (only once!)
        for i in flowerbed:
            if i == 0:
                pot_counter += 1
            if i == 1:
                if pot_counter % 2 == 1:
                    num_plant = (pot_counter - 1) / 2
                elif pot_counter % 2 == 0:
                    if seen_flower == False:
                        n -= 1
                    num_plant = (pot_counter/ 2) - 1
                pot_counter = 0
                seen_flower = True
                n -= num_plant
                if n <= 0:
                    return True
        if pot_counter > 0:
            if pot_counter % 2 == 1:
                if seen_flower == False:
                    n -= 1
                num_plant = (pot_counter - 1) / 2
            elif pot_counter % 2 == 0:
                num_plant = pot_counter/ 2
            n -= num_plant
        if n <= 0:
            return True
        return False