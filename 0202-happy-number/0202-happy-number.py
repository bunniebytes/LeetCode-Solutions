class Solution:
    def isHappy(self, n: int) -> bool:
        seen_set = (2, 3, 4, 5, 6, 8, 9)
        temp_num = n
        while True:
            # seen_set.add(temp_num)
            temp_num = sum([int(x)**2 for x in str(temp_num)])
            if temp_num == 1:
                return True
            if temp_num in seen_set:
                return False
        


        # add number to dictionary
        # convert number into digits and find square of each and then sum (use list)
        # check if new number is 1
        # check dictionary - if in dictionary return false/else add to dictionary

        #2 -  4 16 37 58 89 145 42 20 4