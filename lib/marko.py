import numpy as np
import random

class Marko():
    def __init__(self, seed = 0):
        #Initialize state
        np.random.seed(seed)

    def setWord(self, file_path, encoding = 'utf-8', separator =' '):
        with open(file_path, encoding = encoding) as f:
            self.text_array = f.read().replace('\n', '').replace('.', ' .').replace(',', ' ,').split(separator)
            self.chain = {}
            w1, w2 = '', ''
            for word in self.text_array:
                w1, w2 = w2, word
                if w1 == '':
                    w2 = word
                    continue
                if self.chain.get(w1):
                    if self.chain.get(w1).get(w2):
                        self.chain.get(w1)[w2] += 1
                    else:
                        self.chain.get(w1)[w2] = 1
                else:
                    self.chain[w1] = {w2: 1}
    def gen(self, len):
        w1 = random.choice(list(self.chain.keys()))
        #w1 = 'in'
        w2 = ''
        text = w1
        for i in range(len):
            sub_chain = self.chain.get(w1)
            w2 = random.choice(list(sub_chain.keys()))
            ## Pick up with bias...
            """
            weightslist = sub_chain.values()
            weight = sum(weightslist)
            rand = int(weight * np.random.rand())
            choice = 0
            for (i, w) in enumerate(weightslist):
                if choice < w:
                    choice = i
            w2 = list(sub_chain.keys())[choice]
            """
            text += ' ' + w2
            w1 = w2
        return text
    def __str__(self):
        print(len(self.chain.keys()))
        return str(self.chain)

if __name__ == '__main__':
    marko = Marko()
    marko.setWord('./sample.txt')
    print(marko.gen(500))
