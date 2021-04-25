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
        ptr.end = True
    return root
def print_trie(trie):
    w = open("output.txt", "a")
    for key in trie.children.keys():
        w.write(str(trie.children[key].parent) + "->" + str(trie.children[key].num) + ":" + key + "\n")
        #print(str(trie.children[key].parent) + "->" + str(trie.children[key].num) + ":" + key + "\n")
        print_trie(trie.children[key])
f = open("input.txt", "r")
l = [x.strip() for x in f]
trie = make_trie(l)
print_trie(trie)