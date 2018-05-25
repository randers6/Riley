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
        
        
words2=[]    #rename not word nodes in future 
words='Hello my name is Riley I like to eat cake My cats names are Gus Mable and Felix I live in Mass This summer I will stay in VA I go to school at UMW I study math and studio art I made stuffed peppers for dinner easter was Sunday'    
word=words.split()


for iii in range(len(word)):
    sameword=False
    
    for w in words2:
        
        if word[iii]==w.word:
            sameword=True 
            break
        
    if sameword==False:
        words2.append(WordNode(word[iii]))
        
            
            
for (ii,w) in enumerate(word[:-1]):
    current_node=None 
    for wordnode in words2:
        if w==wordnode.word:
            current_node=wordnode
            break
        
    for wordnode in words2:
        if word[ii+1]==wordnode.word:
            current_node.addNode(wordnode)
                    
                    
        
            
    

    
    
Current=words2[3]
for ii in range(0,3):
    Current.printWord()
    Current = Current.nextWord()

    if Current==None:
        break
    
        



#I need this pick one word from self.nodes then loop back and have that ode be the word. Then continue and print that at the end. 