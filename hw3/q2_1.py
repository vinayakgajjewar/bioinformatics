def bwt(t):
    m = []
    # construct m(t) by prepending suffixes
    for i in range(len(t)):
        cyclic_rotation = t[i:] + t[:i]
        #print(cyclic_rotation)
        m.append(cyclic_rotation)
    m.sort()
    for i in m:
        print(i)
    # get last column in m
    o = open("output.txt", "w")
    last_col = ""
    for rotation in m:
        last_col = last_col + rotation[-1:]
    o.write(last_col)
    print(last_col)
    o.write("\n")

f = open("input.txt")
text = f.readline()
f.close()
bwt(text)