def reverse_array(letters, first=0, last=None):
    if last is None:
        last = len(letters)
    last -= 1
    while first < last:
        letters[first], letters[last] = letters[last], letters[first]
        first += 1
        last -= 1
