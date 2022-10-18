class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0]*n
        for start,end,seats in bookings:
            res[end-1]+=seats
            if start>1:
                res[start-2]-=seats
        for i in range(n-2,-1,-1):
            res[i]+=res[i+1]
        return res
