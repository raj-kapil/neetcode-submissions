class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        lst = [(y,x) for x,y in Counter(nums).items()]
        heap = []
        heapq.heappush(heap, lst[0])
        index = 1

        while index < len(lst):
            heapq.heappush(heap, lst[index])
            if len(heap) > k:
                heapq.heappop(heap)
            index += 1

        res = [y for x,y in heap]

        return res
                