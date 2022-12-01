class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_gas = gas[0]
        result = 0
        worst_case = 0
        
        for x in range(len(gas)):
            current_gas -= cost[x]
            
            if current_gas < worst_case:
                worst_case = current_gas
                result = x+1
            
            if x < len(gas)-1:
                current_gas += gas[x+1]
        
        if current_gas < 0:
            return -1
        else:
            return result
