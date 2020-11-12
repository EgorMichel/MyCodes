while True:

    num = int(input())
    l = 0
    r = 255
    m = (r + l) / 2
    while l + 1 < r:
        if m > num:
            r = m
            m = int((l + r) / 2)
        else:
            l = m
            m = int((l + r) / 2)
    print (m)