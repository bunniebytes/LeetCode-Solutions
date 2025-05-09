class Solution:
    def isHappy(self, n: int) -> bool:
        sum_dict = {}
        temp_num = n
        while True:
            if temp_num == 1:
                return True
            elif temp_num in sum_dict:
                return False
            else:
                sum_dict[temp_num] = 1
                temp_num = sum([int(x)**2 for x in str(temp_num)])
        


        # add number to dictionary
        # convert number into digits and find square of each and then sum (use list)
        # check if new number is 1
        # check dictionary - if in dictionary return false/else add to dictionary

        #2 -  4 16 37 58 89 145 42 20 4