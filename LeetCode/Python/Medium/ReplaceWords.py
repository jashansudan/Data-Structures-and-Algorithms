class Solution(object):
    def replaceWords(self, dict, sentence):
        arr = sentence.split(' ')
        for i in range(len(arr)):
            temp = arr[i]
            for root in dict:
                if (temp[:len(root)] == root):
                    arr[i] = root
                    break
        return ' '.join(arr)
