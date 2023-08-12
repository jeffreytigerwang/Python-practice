# https://leetcode.com/problems/task-scheduler/
import heapq
from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        countHeap = [-x for x in count.values()]
        heapq.heapify(countHeap)

        record = []   # [frequency, ready time]
        time = 0

        while countHeap or record:
            time += 1

            #   Skip waiting time (while loop)
            if not countHeap:
                time = record[0][1]

            else:
                currFreq = heapq.heappop(countHeap) + 1

                if currFreq < 0:
                    record.append([currFreq, time + n])

            #   OR
            # if countHeap:
            #     currFreq = heapq.heappop(countHeap) + 1
            #
            #     if currFreq < 0:
            #         record.append([currFreq, time + n])

            if record and record[0][1] == time:
                heapq.heappush(countHeap, record.pop(0)[0])

        return time


