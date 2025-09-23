class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        num_baskets = len(baskets)
        for fruit in fruits:
            pointer = 0
            while pointer < num_baskets:
                if fruit > baskets[pointer]:
                    pointer += 1
                elif fruit <= baskets[pointer]:
                    del baskets[pointer]
                    num_baskets -= 1
                    break
        return num_baskets