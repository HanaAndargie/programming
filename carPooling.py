class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        minheap=[]
        currpass=0
        for t in trips:
            numpass,start,end=t
            while minheap and minheap[0][0]<=start:
                currpass-=heapq.heappop(minheap)[1]
            currpass+=numpass
            if currpass>capacity:
                return False
            heapq.heappush(minheap,(end,numpass))
        return True
