class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # import heapq
        # lst = [(y,x) for x,y in Counter(nums).items()]
        # heap = []
        # heapq.heappush(heap, lst[0])
        # index = 1

        # while index < len(lst):
        #     heapq.heappush(heap, lst[index])
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        #     index += 1
        # res = [y for x,y in heap]
        # return res
        ##########################################################
        ##########################################################
        ##########################################################
        ##########################################################
        # bucket sort
        freq_counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) +1 )]
        
        for num, freq in freq_counter.items():
            buckets[freq].append(num)
        result = []
        for i in range(len(buckets) -1, 0, -1):
            for x in buckets[i]:
                result.append(x)
                if len(result) == k:
                    return result
        return result
        

          