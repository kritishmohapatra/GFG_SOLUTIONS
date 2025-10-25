import heapq
import numpy as np
class Solution:
     def minOperations(self, arr):
          # code here
          size = len(arr)
          total = sum(arr)
          remaining = total/2
          count = 0

          arr = np.array(arr)
          arr = list(arr * (-1))
          heapq.heapify(arr)

          if size == 0:
               return 0
          elif size == 1:
               return 1
          else:
               while total > remaining:
                    largest = -heapq.heappop(arr)
                    half = largest / 2
                    total -= half

                    heapq.heappush(arr, -half)
                    count += 1
          
          return count