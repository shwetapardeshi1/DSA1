class TrieNode:
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False
  
class Trie: 
    def __init__(self): 
        self.root = TrieNode()
        
    def insert(self,key): 
        tmp = self.root 
        length = len(key) 
        for level in range(length): 
            index = ord(key[level]) - ord('a')
            if not tmp.children[index]: 
                tmp.children[index] = TrieNode()
            tmp = tmp.children[index] 
        tmp.isEndOfWord = True
  
