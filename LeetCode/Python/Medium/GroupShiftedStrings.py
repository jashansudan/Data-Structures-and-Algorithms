class Solution:
    def groupStrings(self, strings):
        string_map = collections.defaultdict(list)
        for string in strings:
            string_map[self.hashString(string)].append(string)

        result = []
        for i in string_map:
            result.append(string_map[i])
        return result

    def hashString(self, string):
        hash = ""
        if len(string) == 1:
            return "0"
        else:
            for i in range(1, len(string)):
                if ord(string[i]) < ord(string[i - 1]):
                    hash += "." + str(26 + (ord(string[i]) - ord(string[i - 1])))
                else:
                    hash += "." + str((ord(string[i]) - ord(string[i - 1])))
            return hash
