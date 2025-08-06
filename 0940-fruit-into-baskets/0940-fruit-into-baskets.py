from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        previous_fruit = None
        fruit_1 = None
        fruit_2 = None
        fruit_1_sum = 0
        fruit_2_sum = 0
        consecutive = 0
        max_sum = 0
        # loop through fruit in fruits
        for fruit in fruits:
            # check if fruit_1 or fruit_2 are fruit:
            if fruit_1 == fruit or fruit_2 == fruit:
                # if previous is same as fruit
                if previous_fruit == fruit:
                    # we add 1 to consecutive
                    consecutive += 1
                elif previous_fruit is not None:
                    consecutive = 1
                if fruit_1 == fruit:
                    fruit_1_sum += 1
                elif fruit_2 == fruit:
                    fruit_2_sum += 1
            if fruit_1 != fruit and fruit_2 != fruit:
                # we check if fruit_1 is same as previous
                if fruit_1 == previous_fruit:
                    # if it is we replace fruit_2
                    fruit_2 = fruit
                    fruit_2_sum = 1
                    fruit_1_sum = consecutive
                # else replace fruit 1 with fruit
                else:
                    fruit_1 = fruit
                    fruit_1_sum = 1
                    fruit_2_sum = consecutive
                consecutive = 1
            # find the new max between max_sum and fruit_1_sum + fruit_2_sum
            max_sum = max(max_sum, fruit_1_sum + fruit_2_sum)
            previous_fruit = fruit
        return max_sum
    