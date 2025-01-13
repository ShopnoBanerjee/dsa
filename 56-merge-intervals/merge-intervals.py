class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []

        intervals.sort(key=lambda x: x[0])
        
        output.append(intervals[0])
        i = 0
        k = 0
        while i < len(intervals)-1:
            if output[k][1] >= intervals[i+1][0]:
                output[k][1] = max(output[k][1],intervals[i+1][1])
                i += 1
            else:
                output.append(intervals[i+1])
                k += 1
                i += 1
    
        return(output)

        