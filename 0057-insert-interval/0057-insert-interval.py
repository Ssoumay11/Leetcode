class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result=[]
        #case interval is comp bef new interval 
        for interval in intervals:
            #case interval is comp bef new interval 
            if interval[1] < newInterval[0]:
                result.append(interval)
            
            # Case 2: interval is completely after newInterval
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        result.append(newInterval)
        
        return result







































        