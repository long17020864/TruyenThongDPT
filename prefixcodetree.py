class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.symbol = None

class PrefixCodeTree:
    def __init__(self):
        self.root = Node()

    def insert(self, codeword, symbol):
        rootNode = self.root
        for el in codeword:
            if el == 1:
                if rootNode.right == None:
                    rootNode.right = Node()
                rootNode = rootNode.right
            elif el == 0:
                if rootNode.left == None:
                    rootNode.left = Node()
                rootNode = rootNode.left
        rootNode.symbol = symbol

    def decode(self, encodedData, datalen):
        listBit = []
        for el in encodedData:
            listBit += bin(el)[2:].zfill(8)

        rootNode = self.root
        count = 0
        message = ""
        tmp = ""
        for bit in listBit:
            tmp += bit
            if count < datalen:
                if bit == '1':
                    rootNode = rootNode.right
                elif bit == '0':
                    rootNode = rootNode.left

                if rootNode.symbol != None:
                    tmp += ' '
                    message += rootNode.symbol + ' '
                    rootNode = self.root
            count += 1
            if count % 8 == 0:
                tmp += '|'
        print(tmp)
        return message

codebook = {
    'x1': [0],
    'x2': [1, 0, 0],
    'x3': [1, 0, 1],
    'x4': [1, 1],
}

codeTree = PrefixCodeTree()

for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

message = codeTree.decode(b'\xd2\x9f\x20', 21)

print(message)