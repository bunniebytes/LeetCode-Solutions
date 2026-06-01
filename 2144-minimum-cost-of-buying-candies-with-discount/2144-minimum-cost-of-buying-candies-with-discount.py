class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # find free_candies, additional using divmod
        free, extra = divmod(len(cost), 3) # dividing by 3 because every 2 get 1 free
        len_cost = len(cost) - extra
        buy = 0
        # sort the cost and reverse list
        cost.sort(reverse = True)
        for idx in range(0, len_cost, 3):
            buy += cost[idx] + cost[idx + 1]
            # free -= 1

        for idx in range(extra):
            buy += cost[len_cost + idx]

        return buy