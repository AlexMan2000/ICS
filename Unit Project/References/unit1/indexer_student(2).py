
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
        try:
            if isinstance(m, str):
                self.msgs.append(m)
            else:
                raise ValueError
        except ValueError:
            print("Cannot add others data types, add a string to the messages.")
            return
        else:
            self.total_msgs += 1

    # add a msg to my log history. update total_msg. parse msg to words, and for each word update the indexing info
    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    """implement
       parse msg "m" with line number "l", update kv pair (word:list of line num) in self.index
    """
    def indexing(self, m, l):
        words = m.split()
        for i in range(len(words)):
            if not words[i].isalnum():
                words[i] = Index.remove_punctuation(words[i])
        words = set(words)
        for w in words:
            try:
                self.index[w].append(l)
            except:
                self.index[w] = [l]
                self.total_words += 1
    @staticmethod
    def remove_punctuation(word):
        output = str()
        for char in word:
            if char.isalnum():
                output += char
        return output
    
    # implement: query interface
    """return a list of tupple. if index the first sonnet (p1.txt), then
    call this function with term 'thy' will return the following:
    [(7, " Feed'st thy light's flame with self-substantial fuel,"),
    (9, ' Thy self thy foe, to thy sweet self too cruel:'),
    (9, ' Thy self thy foe, to thy sweet self too cruel:'),
    (12, ' Within thine own bud buriest thy content,')]"""
    def search(self, term):
        msgs = []
        try:
            for index in self.index[term]:
                msgs.append((index+1, self.msgs[index]))
        except KeyError:
            return tuple()
        else:
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
       file = open(self.name, "r")
       while True:
           line = file.readline()
           if len(line) == 0:
               break
           else:
               line = line.strip()
               if len(line) > 0:
                   self.add_msg_and_index(line)
    
    """implement: p is an integer, get_poem(1) returns a list,
       each item is one line of the 1st sonnet
    """
    # hint: to get poem indexed with III.
    # start from the line that contains word "III."
    # end before the line that contains word "IV."
    def get_poem(self, p):
        poem = []
        number = 0
        for i in range(1,self.get_msg_size()):
            if self.int2roman[number+1] == Index.remove_punctuation(self.get_msg(i)):
                number += 1
                poem.append([])
            poem[number - 1].append(self.get_msg(i))
            
        return poem[p-1]

if __name__ == "__main__":
    sonnets = PIndex("AllSonnets.txt")
    # the next two lines are just for testing
    p3 = sonnets.get_poem(3)
    s_love = sonnets.search("love")