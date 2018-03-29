


class WordNode:
    def __init__(self, word):
        self.word=word
        
        
          
    def addNode(self, word): #this is where I am stuck. I know I need to use word but I dont know how 
        word_2=WordNode("I")
        
    def nextWord(self):
        return('{}{}'.format(self.word_1,self.word_2))


    #def printWord(self):
        
        
word_1=WordNode("I")
word_2=WordNode("am")

print(word_1.addNode())