
def find_missing(first, second):
  len_first = len(first)
  len_second = len(second)
  if len_first == len_second:
    return 0
  else:
    for i in second:
      if i not in first:
        return i
    for item in first:
      if item not in first:
        return item


print find_missing([], [])
print find_missing([2], [2])
print find_missing([1, 2], [1, 2, 5])