class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        final_end = float("inf")
        land = sorted(list(zip(landStartTime, landDuration)))
        water = sorted(list(zip(waterStartTime, waterDuration)))
        len_water = len(water)
        len_land = len(land)

        for w in range(len_water):
            w_start, w_duration = water[w]
            w_end = w_start + w_duration
            for l in range(len_land):
                l_start, l_duration = land[l]
                l_end = l_start + l_duration
                if l_end >= w_start:
                    water_final = l_end + w_duration
                else:
                    water_final = w_start + w_duration

                if water_final < final_end:
                    final_end = water_final

                if w_end >= l_start:
                    land_final = w_end + l_duration
                else:
                    land_final = l_start + l_duration

                if land_final < final_end:
                    final_end = land_final

        return final_end