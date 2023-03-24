def mdc(x,y):
    if x == 0 or y == 0:
        return 1
    else:
        return mdc(y, x % y)
result = mdc(0, 0)
print(result)