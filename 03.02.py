def frange(val, base=0.0, step=0.1):
    if val < base:
        result = fillfrange(val, base, step)
    else:
        result = fillfrange(base, val, step)
    return result
def fillfrange(start, stop, step):
    result = []
    while True:
        if (start > stop):
            break
        result.append(start)
        start += step
    return result
print(frange(2))
print(frange(1, 2.0))
print(frange(1.0, 3.0, 3.5))
