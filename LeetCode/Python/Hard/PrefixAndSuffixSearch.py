class WordFilter(object):
    def __init__(self, words):
        self.pre_suf_map = {}
        for word in range(len(words)):
            length = len(words[word])
            for i in range(length + 1):
                for j in reversed(range(length + 1)):
                    if (i > 10 or (length - j) > 10) > length:
                        continue
                    comb = words[word][:i] + "." + words[word][j:]
                    self.pre_suf_map[comb] = word

    def f(self, prefix, suffix):
        pref_suf = prefix + "." + suffix
        if pref_suf in self.pre_suf_map:
            return self.pre_suf_map[pref_suf]
        return -1
