class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        for i in range(1, len(gain)):
            gain[i] = gain[i] + gain[i - 1]

        return max(0, max(gain))