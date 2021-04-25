bwt = "TTCCTAACG$A"
def reverse_bwt(t):
    table = [""] * len(t)
    for i in range(len(t)):
        table = [t[i] + table[i] for i in range(len(t))]
        #print("unsorted:", table)
        table = sorted(table)
        #print("sorted:", table)
        r_bwt = [row for row in table if row.endswith("$")][0]
        print("curr:", r_bwt)
    print("final:", r_bwt)
    o = open("output.txt", "w")
    o.write(r_bwt)

f = open("input.txt")
text = f.readline()
f.close()
reverse_bwt(text)