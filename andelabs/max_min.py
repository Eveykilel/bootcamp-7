
def find_max_min(x):
    a = min (x)
    b = max (x)

    if a == b:
      return [len(x)]
    return [a, b]