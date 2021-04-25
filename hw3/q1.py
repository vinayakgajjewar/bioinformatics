class Suffix:
    index = 0
    suffix = ""
def suffix_sort(s):
    return s.suffix
def suffix_array(t):
    sa = []
    for i in range(len(t)):
        s = Suffix()
        s.index = i
        s.suffix = t[i:]
        sa.append(s)
    sa.sort(key=suffix_sort)
    o = open("output.txt", "w")
    for i in range(len(sa) - 1):
        o.write(str(sa[i].index) + ", ")
    o.write(str(sa[len(sa) - 1].index))
    o.write("\n")
    o.close()
f = open("input.txt")
text = f.readline()
f.close()
suffix_array(text)