


class WordNode:
    def __init__(self, word):
        self.word=word
        self.nodes=[]      #this makes an instance variable: different list for each word? 
        
          
    def addNode(self, nodes): 
        self.nodes.append(nodes)
        
    def nextWord(self):
        return('{}{}'.format(self.word,self.nodes))  #this gives back all the words that can possibly come after


    def printWord(self):
        print()
        
        
word_1=WordNode("I")
word_1.addNode("am")
word_1.addNode("want")

word_2=WordNode("am")
word_2.addNode("hungry")

word_3=WordNode("hungry")

word_4=WordNode("want")
word_4.addNode("food")

word_5=WordNode("food")

print(word_1.nextWord())