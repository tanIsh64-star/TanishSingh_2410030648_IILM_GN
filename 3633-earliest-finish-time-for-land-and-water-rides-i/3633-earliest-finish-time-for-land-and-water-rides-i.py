class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        min_land_end = float('inf')

        for i in range(len(landStartTime)):
            min_land_end = min(min_land_end, landStartTime[i] + landDuration[i])

        ans = float('inf')

        for j in range(len(waterStartTime)):
            ans = min(ans, max(min_land_end, waterStartTime[j]) + waterDuration[j])

        min_water_end = float('inf')

        for j in range(len(waterStartTime)):
            min_water_end = min(min_water_end, waterStartTime[j] + waterDuration[j])

        for i in range(len(landStartTime)):
            ans = min(ans, max(min_water_end, landStartTime[i]) + landDuration[i])

        return ans