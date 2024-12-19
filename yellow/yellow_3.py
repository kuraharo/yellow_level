class Solution(object):
    def merge(self,intervals):
        i=0
        intervals.sort(key=lambda x: x[0])
        while len(intervals)>1:
            if(i+1>len(intervals)-1):
                return intervals
            if(intervals[i][1]>=intervals[i+1][0] and intervals[i][0]<=intervals[i+1][0] and intervals[i][1]<=intervals[i+1][1]):
                intervals[i].remove(intervals[i][1])
                intervals[i].append(intervals[i+1][1])
                intervals.remove(intervals[i+1])
                i=i-1
            if(intervals[i+1][0]<intervals[i][0] and intervals[i+1][1]>=intervals[i][1]):
                intervals.remove(intervals[i])
            if(intervals[i][0]<=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1] and intervals[i]!=intervals[i+1]):
                intervals.remove(intervals[i+1])
                i=i-1
            i+=1
        return intervals