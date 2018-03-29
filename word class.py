import random


class WordNode:
    def __init__(self, word):
        self.word=word
        self.nodes=[]      #this makes an instance variable
        
          
    def addNode(self, nodes): 
        self.nodes.append(nodes)
        
    def nextWord(self):#check if empty 
        if self.nodes==[]:
            return(None)
        else:
            
            r=random.choice(self.nodes)
            return(r) #this gives back all the words that can possibly come after I wat just one word 
#am going to use a random number generator to pick a random slot in self.nodes

    def printWord(self):
        print(self.word)

     
word=[]      
word.append(WordNode("I")) # this worked before random pick why???something to do with importing random? 
word.append(WordNode("am"))
word.append(WordNode("hungry"))
word.append(WordNode("want"))
word.append(WordNode("food"))

word[0].addNode(word[1])
word[0].addNode(word[3])
word[1].addNode(word[2])
word[3].addNode(word[4])

print(word[1].nextWord())


Current=word[1]
for ii in range(0,3):
    Current.printWord()
    Current = Current.nextWord()

    if Current==None:
        break
    
        



#I need this pick one word from self.nodes then loop back and have that ode be the word. Then continue and print that at the end. 