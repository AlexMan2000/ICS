
import pickle

class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = []    # list to store msg
        self.index = {}   # dict mapping word to list of line number
        self.total_msgs = 0
        self.total_words = 0
        
    def get_total_words(self):
        return self.total_words
        
    def get_msg_size(self):
        return self.total_msgs
        
    def get_msg(self, n):
        return self.msgs[n]
        
    # implement
    """ update self.msgs and self.total_msgs 
    """
    def add_msg(self, m):
        self.msgs.append(m)
        self.total_msgs+=1

    # add a msg to my log history. update total_msg. parse msg to words, and for each word update the indexing info
    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    """implement  
       parse msg "m" with line number "l", update kv pair (word:list of line num) in self.index
    """
    def indexing(self, m, l):
        m_wordlist=m.split(' ')
        for word in m_wordlist:
            if word in self.index:
                self.index[word].append(l)
            else:
                self.index[word]=[]
                self.index[word].append(l)
    
    # implement: query interface
    """return a list of tupple. if index the first sonnet (p1.txt), then
    call this function with term 'thy' will return the following:
    [(7, " Feed'st thy light's flame with self-substantial fuel,"),
    (9, ' Thy self thy foe, to thy sweet self too cruel:'),
    (9, ' Thy self thy foe, to thy sweet self too cruel:'),
    (12, ' Within thine own bud buriest thy content,')]"""
    def search(self, term):
        msgs = []
        if term in self.index:
            numberlist = self.index[term]
            for number in numberlist:
                msgs.append((number,self.msgs[number]))
        else:
            msgs.append((None,None))
        return msgs

class PIndex(Index):
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems() # will be executed after the class is created
        
    """implement: 1) open the file for read,  
       for each line call the add_msg_and_index method which will
        # 1. assign the line to a line number
        # 2. parse the line to words
        # 3. for each word, update the indexing info 
    """
    def load_poems(self):
        f=open('Allsonnets.txt','r')
        poems=[]
        for line in f:
            poems.append(line.strip())
        f.close()
        for line in poems:
            Index.add_msg_and_index(self,line)
       
    
    """implement: p is an integer, get_poem(1) returns a list,
       each item is one line of the 1st sonnet
    """
    # hint: to get poem indexed with III.
    # start from the line that contains word "III."
    # end before the line that contains word "IV."
    def get_poem(self, p):
        poem = []
        romannum=self.int2roman[p]
        romannext=self.int2roman[p+1]
        tag=romannum + '.'
        tagnext=romannext+'.'
        taglinenum=Index.search(self,tag)[0][0]
        tagnextlinenum=Index.search(self,tagnext)[0][0]
        if tagnextlinenum == None:
            for i in range(taglinenum,self.total_msgs+1):
                poem.append(self.msgs[i])
        else:
            for i in range(taglinenum,tagnextlinenum):
                poem.append(self.msgs[i])
        
        return poem

if __name__ == "__main__":
    sonnets = PIndex("AllSonnets.txt")
    # the next two lines are just for testing
    p3 = sonnets.get_poem(3)
    p1 = sonnets.get_poem(1)
    s_love = sonnets.search("love")
    print('p3',p3)
    print('p1',p1)
    print('s_love',s_love)