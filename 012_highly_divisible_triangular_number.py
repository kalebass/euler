def res():
    def triangles():
        t = 1
        diff = 2
        while True:
            yield t
            t += diff
            diff += 1
    
    for tri in triangles():
        divisor_count = 0
        for divisor in range(1, int(tri ** 0.5)):
            if tri % divisor == 0:
                divisor_count += 2
        if divisor_count >= 500:
            return tri

print(res())
