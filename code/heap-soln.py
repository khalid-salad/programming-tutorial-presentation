popped = []  # store popped heap values
prev, min_count = heappop(heap)
for i in range(k - 1):
  if not heap:  # ran out of elements
    return False
  else:
      value, count = heappop(heap)
      if value != prev + 1:  # not consecutive
        return False
      else:
        count -= min_count
        prev = value
        if count > 0:
          popped.append((value, count))
for val in popped:
    heappush(heap, val)
