class Trie(object):

    def __init__(self):
        self.root = TrieNode(" ")

    def insert(self, word):
        self.put(word, self.root)

    def put(self, word, node):
        if word == "":
            node.isWord = True
        else:
            if word[0] not in node.char_dict:
                node.char_dict[word[0]] = TrieNode(word[0])
            self.put(word[1:], node.char_dict[word[0]])

    def search(self, word):
        return self.dfsEntireWord(word, self.root)

    def dfsEntireWord(self, word, node):
        if word == "" and node.isWord:
            return True
        elif word == "":
            return False
        else:
            if word[0] not in node.char_dict:
                return False
            else:
                return self.dfsEntireWord(word[1:], node.char_dict[word[0]])

    def startsWith(self, prefix):
        return self.dfsPrefix(prefix, self.root)

    def dfsPrefix(self, prefix, node):
        if prefix == "":
            return True
        else:
            if prefix[0] not in node.char_dict:
                return False
            else:
                return self.dfsPrefix(prefix[1:], node.char_dict[prefix[0]])


class TrieNode(object):
    def __init__(self, let):
        self.char_dict = {}
        self.isWord = False
        self.letter = let
