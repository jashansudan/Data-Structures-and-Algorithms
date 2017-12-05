class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode(" ")

    def addWord(self, word):
        self.insert(word, self.root)

    def insert(self, word, node):
        if len(word) == 0:
            node.isWord = True
        else:
            if word[0] not in node.char_dict:
                node.char_dict[word[0]] = TrieNode(word[0])
            self.insert(word[1:], node.char_dict[word[0]])
        return

    def search(self, word):
        return self.dfs(word, self.root)

    def dfs(self, word, node):
        if word == "" and node.isWord:
            return True
        elif word == "":
            return False
        else:
            if word[0] == ".":
                for i in node.char_dict:
                    if self.dfs(word[1:], node.char_dict[i]):
                        return True
                return False
            else:
                if word[0] in node.char_dict:
                    return self.dfs(word[1:], node.char_dict[word[0]])
                else:
                    return False


class TrieNode(object):
    def __init__(self, let):
        self.char_dict = {}
        self.isWord = False
        self.letter = let
