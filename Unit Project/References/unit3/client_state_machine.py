
from chat_utils import *
import json
import main_run
import random



class ClientSM:
    def __init__(self, s):
        self.state = S_OFFLINE
        self.peer = ''
        self.me = ''
        self.out_msg = ''
        self.s = s
        self.positions = ''

        # socket for the current client

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_myname(self, name):
        self.me = name

    def get_myname(self):
        return self.me

    def start_game(self,peer):
        for i in range(60):
            if i % 2 == 0:
                n = random.randint(1,19)
                self.positions += str(n) + ' '
            else:
                n = random.randint(1,29)
                self.positions += str(n) + ' '
        msg = json.dumps({"action":"game","target":peer, "pos": self.positions})
        mysend(self.s,msg)
        response = json.loads(myrecv(self.s))
        if response["status"] == "success":
            self.peer = peer
            return True
        else:
            self.out_msg += "Connect failed"
        return False


    def connect_to(self, peer):
        msg = json.dumps({"action":"connect", "target":peer})
        mysend(self.s, msg)
        response = json.loads(myrecv(self.s))
        if response["status"] == "success":
            self.peer = peer
            self.out_msg += 'You are connected with '+ self.peer + '\n'
            return (True)
        elif response["status"] == "busy":
            self.out_msg += 'User is busy. Please try again later\n'
        elif response["status"] == "self":
            self.out_msg += 'Cannot talk to yourself (sick)\n'
        else:
            self.out_msg += 'User is not online, try again later\n'
        return(False)

    def disconnect(self):
        msg = json.dumps({"action":"disconnect"})
        mysend(self.s, msg)
        self.out_msg += 'You are disconnected from ' + self.peer + '\n'
        self.peer = ''

    def proc(self, my_msg, peer_msg):
        """
        :param my_msg:
        :param peer_msg:
        :return: self.out_msg: which will be displayed on the client side
        """

        self.out_msg = ''
#==============================================================================
# Once logged in, do a few things: get peer listing, connect, search
# And, of course, if you are so bored, just go
# This is event handling instate "S_LOGGEDIN"
#==============================================================================
        if self.state == S_LOGGEDIN:
            # todo: can't deal with multiple lines yet
            if len(my_msg) > 0:

                if my_msg == 'q':
                    self.out_msg += 'See you next time!\n'
                    self.state = S_OFFLINE

                elif my_msg == 'time':
                    mysend(self.s, json.dumps({"action":"time"}))
                    time_in = json.loads(myrecv(self.s))["results"]
                    self.out_msg += "Time is: " + time_in

                elif my_msg == 'who':
                    mysend(self.s, json.dumps({"action":"list"}))
                    logged_in = json.loads(myrecv(self.s))["results"]
                    self.out_msg += 'Here are all the users in the system:\n'
                    self.out_msg += logged_in

                elif my_msg[0] == 'c':
                    peer = my_msg[1:]
                    peer = peer.strip()
                    if self.connect_to(peer) == True:
                        self.state = S_CHATTING
                        self.out_msg += 'Connect to ' + peer + '. Chat away!\n\n'
                        self.out_msg += '-----------------------------------\n'
                    else:
                        self.out_msg += 'Connection unsuccessful\n'

                elif my_msg[0] == '?':
                    term = my_msg[1:].strip()
                    mysend(self.s, json.dumps({"action":"search", "target":term}))
                    search_rslt = json.loads(myrecv(self.s))["results"].strip()
                    if (len(search_rslt)) > 0:
                        self.out_msg += search_rslt + '\n\n'
                    else:
                        self.out_msg += '\'' + term + '\'' + ' not found\n\n'

                elif my_msg[0] == 'p' and my_msg[1:].isdigit():
                    poem_idx = my_msg[1:].strip()
                    mysend(self.s, json.dumps({"action":"poem", "target":poem_idx}))
                    poem = json.loads(myrecv(self.s))["results"]
                    if (len(poem) > 0):
                        self.out_msg += poem + '\n\n'
                    else:
                        self.out_msg += 'Sonnet ' + poem_idx + ' not found\n\n'

                elif my_msg[0] == 's':
                    peer = my_msg[1:]
                    peer = peer.strip()
                    if self.start_game(peer) == True:

                        self.state = S_GAMING1
                        self.out_msg += 'Gluttonous Snake Game with ' + peer + ' started!\n\n'
                        self.out_msg += 'Your snake will be blue.\n'
                        self.out_msg += 'Please use direction keys to control the movement of your snake.\n\n'
                    else:
                        self.msg += 'Game failed to start！\n\n'
                else:
                    self.out_msg += menu


            if len(peer_msg) > 0:
                try:
                    peer_msg = json.loads(peer_msg)
                except Exception as err :
                    self.out_msg += " json.loads failed " + str(err)
                    return self.out_msg

                if peer_msg["action"] == "connect":
                    # ----------your code here------#

                    self.peer = peer_msg["from"]
                    self.out_msg += 'Request from ' + self.peer + '\n'
                    self.out_msg += 'You are connected with ' + self.peer
                    self.out_msg += '. Chat away!\n\n'
                    self.out_msg += '------------------------------------\n'
                    self.state = S_CHATTING
                    # ----------end of your code----#
                if peer_msg["action"] == "game":
                    self.peer = peer_msg["from"]

                    self.out_msg += self.peer + ' just started a game with you! Enjoy!\n\n'
                    self.out_msg += 'Your snake will be black.\n'
                    self.out_msg += 'Please use W/S/A/D keys to control the movement of your snake.\n\n'

                    self.positions = peer_msg['pos']
                    self.state = S_GAMING2



#==============================================================================
# Start chatting, 'bye' for quit
# This is event handling instate "S_CHATTING"
#==============================================================================
        elif self.state == S_CHATTING:
            if len(my_msg) > 0:     # my stuff going out
                mysend(self.s, json.dumps({"action":"exchange", "from":"[" + self.me + "]", "message":my_msg}))
                if my_msg == 'bye':
                    self.disconnect()
                    self.state = S_LOGGEDIN
                    self.peer = ''
            if len(peer_msg) > 0:  # peer's stuff, coming in
                # ----------your code here------#
                peer_msg = json.loads(peer_msg)
                if peer_msg["action"] == "connect":
                    self.out_msg += "(" + peer_msg["from"] + " joined)\n"
                elif peer_msg["action"] == "disconnect":
                    self.out_msg += peer_msg["message"]
                    self.state = S_LOGGEDIN
                else:
                    self.out_msg += peer_msg["from"] + peer_msg["message"]
                # ----------end of your code----#
            if self.state == S_LOGGEDIN:
                # Display the menu again
                self.out_msg += menu



        elif self.state == S_GAMING1:
            main_run.main(self.me, self.peer, self.me, self.s, self.peer, mysend, myrecv, self.positions)


        elif self.state == S_GAMING2:
            main_run.main(self.peer, self.me, self.me, self.s, self.peer, mysend, myrecv, self.positions)



#==============================================================================
# invalid state
#==============================================================================
        else:
            self.out_msg += 'How did you wind up here??\n'
            print_state(self.state)

        return self.out_msg
