class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        final_end = float("inf")
        # land = list(zip(landStartTime, landDuration))
        # water = list(zip(waterStartTime, waterDuration))
        len_water = len(waterStartTime)
        len_land = len(landStartTime)
        min_land = float("inf")
        min_water = float("inf")

        for idx in range(len_land):
            curr_time = landStartTime[idx] + landDuration[idx]
            if curr_time < min_land:
                min_land = curr_time
                
        for idx in range(len_water):
            curr_time = waterStartTime[idx] + waterDuration[idx]
            if curr_time < min_water:
                min_water = curr_time
        
        for idx in range(len_water):
            water_start = waterStartTime[idx]
            if min_land >= water_start:
                curr_time = min_land + waterDuration[idx]
            else:
                curr_time = water_start + waterDuration[idx]
            
            if curr_time < final_end:
                final_end = curr_time

        for idx in range(len_land):
           land_start = landStartTime[idx]
           if min_water >= land_start:
               curr_time = min_water + landDuration[idx]
           else:
               curr_time = land_start + landDuration[idx]
           
           if curr_time < final_end:
               final_end = curr_time

        return final_end