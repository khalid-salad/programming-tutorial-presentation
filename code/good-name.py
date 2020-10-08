def quick_sort(array):
  if len(array) <= 1:
    return array
  else:
    left, right = [], []
    pivot = array[0]
    for ele in array:
      if ele < pivot:
        left.append(ele)
      else:
        right.append(ele)
    return quick_sort(left) + quick_sort(right)
