class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time_wait = 0
        time = customers[0][0]
        num_cust = len(customers)

        for customer in customers:
            time_arr, time_make = customer
            if time >= time_arr:
                time += time_make
                time_wait += time - time_arr
            else:
                time = time_arr + time_make
                time_wait += time_make

        return time_wait/num_cust