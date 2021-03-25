def task(array):
    l = -1
    r = len(array)
    while r > l + 1:
        m = (l + r) // 2
        if array[m] == '0':
            r = m
        else:
            l = m
    return r

print(task("111111111111111111111111100000000")) 
#O(log2n)   
