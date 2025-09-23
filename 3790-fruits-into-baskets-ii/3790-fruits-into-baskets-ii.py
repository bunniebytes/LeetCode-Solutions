class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        for fruit in fruits:
            pointer = 0
            while pointer < len(baskets):
                if fruit > baskets[pointer]:
                    pointer += 1
                elif fruit <= baskets[pointer]:
                    del baskets[pointer]
                    break
        return len(baskets)