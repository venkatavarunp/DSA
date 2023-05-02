# Trie (Prefix Tree)
The goal of a prefix tree is to achieve
` Insert word in O(n)`,` Search word in O(1)`,`Search prefix word in O(1)` where n is size of word.

this can be used in autocomplete 

![image](https://user-images.githubusercontent.com/130353146/235669851-cff0003d-889b-4b16-b3ad-3a44d23f3524.png)

```python
class TrieNode:
    create a hashmap for each letter in word
    create a value to indicate end of word 
class Trie:
    create a empty root
    def insert(word):
        current node=root node #starting from root node
        for child in word:
            if child not in current.children #hashmap:
                current.children[child]=TrieNode #creating empty root
            current=current.children[child]
        current.word=True #marking end of word
    def search(word):
        current node=root node #starting from root node
        for child in word:
            if child not in current.children:
                return False
                

class TrieNode:
    def __init__(self):
        self.children = {} # creating a hashmap for each letter in word
        self.word = False # value creataed to indicate end of word

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() # create new word
            curr = curr.children[c] 
        curr.word = True # marking end of word

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
```
