class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        max_fuel = 0
        max_fuel_index = 0
        for i in range(len(gas)):
            if gas[i] > max_fuel:
                max_fuel_index = i
                max_fuel = gas[i]
        
        tank = max_fuel
        return max_fuel_index


        

