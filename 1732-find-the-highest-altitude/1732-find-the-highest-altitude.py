class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0

        for num in gain:
            altitude += num
            highest = max(highest, altitude)
        
        return highest
