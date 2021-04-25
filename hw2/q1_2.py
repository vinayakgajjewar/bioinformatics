class Node:
    def __init__(self):
        self.children = {}
        self.num = 0
        self.parent = 0
        self.end = False
def make_trie(words):
    root = Node()
    num = 1
    for word in words:
        ptr = root
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter] = Node()
                ptr.children[letter].num = num
                ptr.children[letter].parent = ptr.num
                num = num + 1
            ptr = ptr.children[letter]
        #print("SETTING PTR.END=TRUE")
        ptr.end = True
    return root

def print_trie(trie):
    w = open("output.txt", "a")
    for key in trie.children.keys():
        w.write(str(trie.children[key].parent) + "->" + str(trie.children[key].num) + ":" + key + "\n")
        print_trie(trie.children[key])

def prefix_matching(trie, word):
    v = trie
    i = 0
    while True:
        char = word[i]
        if char in v.children and v.children[char].end == True:
            return True
        elif char in v.children:
            v = v.children[char]
            i = i + 1
        else:
            #print("match not found")
            return False

f = open("test_input.txt", "r")
text = f.readline().strip()
l = [x.strip() for x in f]
t = make_trie(l)
#print_trie(t)

w = open("output.txt", "a")
i = 0
while text != "":
    if prefix_matching(t, text):
        w.write(str(i) + " ")
    text = text[1:]
    i = i + 1