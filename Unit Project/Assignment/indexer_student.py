import pickle


class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = []
        """
        ["1st_line", "2nd_line", "3rd_line", ...]
        Example:
        "How are you?\nI am fine.\n" will be stored as
        ["How are you?", "I am fine." ]
        """

        self.index = {}
        """
        {word1: [line_number_of_1st_occurrence,
                 line_number_of_2nd_occurrence,
                 ...]
         word2: [line_number_of_1st_occurrence,
                  line_number_of_2nd_occurrence,
                  ...]
         ...
        }
        """

        self.total_msgs = 0
        self.total_words = 0

    def get_total_words(self):
        return self.total_words

    def get_msg_size(self):
        return self.total_msgs

    def get_msg(self, n):
        return self.msgs[n]

    def add_msg(self, m):
        """
        m: the message to add

        updates self.msgs and self.total_msgs
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        self.msgs.append(m.strip())
        self.total_msgs += 1

        # ---- end of your code --- #
        return

    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    def indexing(self, m, l):
        """
        updates self.total_words and self.index
        m: message, l: current line number
        """

        # IMPLEMENTATION
        # ---- start your code ---- #

        # (Improved)Strip the non-character and characters that contains non-alphabetic characters.
        m = m.strip()
        words_list = []
        for index in range(len(m)-1,-1,-1):
            if m[index].isalpha():
                words_list = m[:index+1].split(' ')
                break
        for word in words_list[:]:
            if not word.isalpha():
                words_list.remove(word)


        #Original
        # words_list = m.strip().split(' ')


        for word in words_list:
            self.index[word] = self.index.get(word,[])
            #Avoiding duplicates
            if l not in self.index[word]:
                self.index[word].append(l)

        # ---- end of your code --- #
        return

    # implement: query interface

    def search(self, term):
        """
        return a list of tupple.
        Example:
        if index the first sonnet (p1.txt),
        then search('thy') will return the following:
        [(7, " Feed'st thy light's flame with self-substantial fuel,"),
         (9, ' Thy self thy foe, to thy sweet self too cruel:'),
         (9, ' Thy self thy foe, to thy sweet self too cruel:'),
         (12, ' Within thine own bud buriest thy content,')]
        """
        msgs = []
        # IMPLEMENTATION
        # ---- start your code ---- #
        #Search_words
        if len(term.split()) == 1:
            for k,v in self.index.items():
                if k == term:
                    for index in v:
                        msgs.append((index,self.msgs[index]))

        # (Improved)Search Phrases
        else:
            splited = term.split()
            #Word numbers
            tmp = []
            for item in splited:
                tmp.extend(self.index[item])
            #Return a list(tmp2) which contains the index that appears more than once.
            tmp.sort()
            tmp2 = []
            for i in range(1,len(tmp)):
                if tmp[i] == tmp[i-1]:
                    tmp2.append(tmp[i])
            #return the search result for phrases.
            for index in tmp2:
                if self.msgs[index].find(term) != -1:
                    msgs.append((index,term))


        # ---- end of your code --- #
        return msgs


class PIndex(Index):
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems()

    def load_poems(self):
        """
        open the file for read, then call
        the base class's add_msg_and_index()
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        allSonnets = open(self.name,'r')
        for line in allSonnets:

            self.add_msg_and_index(line)
        allSonnets.close()

        # ---- end of your code --- #
        return

    def get_poem(self, p):
        """
        p is an integer, get_poem(1) returns a list,
        each item is one line of the 1st sonnet

        Example:
        get_poem(1) should return:
        ['I.', '', 'From fairest creatures we desire increase,',
         " That thereby beauty's rose might never die,",
         ' But as the riper should by time decease,',
         ' His tender heir might bear his memory:',
         ' But thou contracted to thine own bright eyes,',
         " Feed'st thy light's flame with self-substantial fuel,",
         ' Making a famine where abundance lies,',
         ' Thy self thy foe, to thy sweet self too cruel:',
         " Thou that art now the world's fresh ornament,",
         ' And only herald to the gaudy spring,',
         ' Within thine own bud buriest thy content,',
         " And, tender churl, mak'st waste in niggarding:",
         ' Pity the world, or else this glutton be,',
         " To eat the world's due, by the grave and thee.",
         '', '', '']
        """
        poem = []
        # IMPLEMENTATION
        # ---- start your code ---- #
        #Convert the integers to Roman numbers

        #Improved logic
        beginning = self.search(self.int2roman[p])[0][0]
        try:
            ending = self.search(self.int2roman[p + 1])[0][0]
        except:
            ending = None
        poem.append(self.int2roman[p]+'.')


        #Original
        # beginning = self.search(self.int2roman[p]+'.')[0][0]
        # ending = self.search(self.int2roman[p+1]+'.')[0][0] if p+1 < len(self.int2roman) else None

        if ending:
            poem.extend(self.msgs[beginning+1:ending])
        else:
            poem.extend(self.msgs[beginning+1:])

        # ---- end of your code --- #
        return poem


if __name__ == "__main__":
    sonnets = PIndex("AllSonnets.txt")
    # the next two lines are just for testing
    p3 = sonnets.get_poem(3)
    print(p3)
    s_love = sonnets.search("love")
    print(s_love)

    #Personal test
    s_who = sonnets.search("who")
    print(s_who)
    s_five = sonnets.search("five")
    print(s_five)
    # test for multi
    s_phrase = sonnets.search("took up")
    print(s_phrase)
