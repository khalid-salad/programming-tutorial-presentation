while counts:  # dictionary to store counts
  x = min(counts)
  min_count = counts[x]
  del counts[x]  # remove smallest
  for i in range(1, k):
      if counts[x + i] < min_count:
        return False
      else:
        counts[x + i] -= min_count
        if counts[x + i] == 0:
          del counts[x + i]