class Solution:
    def isValid(self, s: str) -> bool:
        closed = [")", "]", "}"]
        valid = ["()", "[]", "{}"]
        temp = []
        #iterate through the string:
        for x in s:
            #if bracket is not in the closed:
            if x not in closed:
                #add to list
                temp.append(x)
            #else (if bracket in closed):
            else:
                #checking if there are items in the list meaning open bracket before
                if len(temp) == 0:
                    return False
                #check if last item in list + closed bracket in valid:
                # if valid:
                bracket = temp.pop() + x
                if bracket not in valid:
                    return False
        #if list has items in it: (after iterating through we want the list to be empty/None)
        if len(temp) > 0:
            return False
        return True