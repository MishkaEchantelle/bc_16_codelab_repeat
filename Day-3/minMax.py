def find_max_min(data):

    min_max = [min(data), max(data)]

    if min(data) == max(data):
        return [min(data)]
    else:
        return min_max
  