def seedLCG(initVal):
    global rand
    rand = initVal

def lcg():
    a = 37
    c = 1
    m = 64
    global rand
    rand = (a*rand + c) % m
    return rand

seedLCG(200)

for i in range(10):
    print (lcg())