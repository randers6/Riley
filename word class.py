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
        
        
words2=[]
words='Python Is an easy to learn powerful programming language It has efficient high-level data structures And a simple but effective approach to Object-oriented programming Python’s elegant syntax And dynamic typing together With its interpreted nature make it an ideal language For scripting And rapid application development In many areas on most platforms'    
word=words.split()

for iii in range(len(word)):
     words2.append(WordNode(word[iii]))
#need t orecognize repeated nodes, this doesnt 

for rr in range(len(words2)-1):
    words2[rr].addNode(words2[rr+1])
    
    
Current=words2[0]
for ii in range(0,5):
    Current.printWord()
    Current = Current.nextWord()

    if Current==None:
        break
    
        



#I need this pick one word from self.nodes then loop back and have that ode be the word. Then continue and print that at the end. 