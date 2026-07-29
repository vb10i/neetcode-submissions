class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr = 0
        total = 0

        for arr,order in customers:
            if arr < curr:
                total += curr-arr
            else:
                curr = arr 
            total += order
            curr += order
        return total/len(customers)