class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelivin = celsius + 273.15

        fahrenheit = celsius * 1.80 + 32

        return [kelivin, fahrenheit]