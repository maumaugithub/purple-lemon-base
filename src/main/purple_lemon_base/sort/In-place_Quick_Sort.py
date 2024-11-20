def inplace_quick_sort(L, a, b):
  """Sort the list from L[a] to L[b] inclusive using the quick-sort algorithm."""
  if a >= b: return                                      # range is trivially sorted
  pivot = L[b]                                           # last element of range is pivot
  left = a                                               # will scan rightward
  right = b-1                                            # will scan leftward
  while left <= right:
    # scan until reaching value equal or larger than pivot (or right marker)
    while left <= right and L[left] < pivot:
      left += 1
    # scan until reaching value equal or smaller than pivot (or left marker)
    while left <= right and pivot < L[right]:
      right -= 1
    if left <= right:                                    # scans did not strictly cross
      L[left], L[right] = L[right], L[left]              # swap values
      left, right = left + 1, right - 1                  # shrink range

  # put pivot into its final place (currently marked by left index)
  L[left], L[b] = L[b], L[left]
  # make recursive calls
  inplace_quick_sort(L, a, left - 1)
  inplace_quick_sort(L, left + 1, b)
