S_ALONE = 0
S_TALKING = 1

# ==============================================================================
# Group class:
# member fields:
#   - An array of items, each a Member class
#   - A dictionary that keeps who is a chat group
# member functions:
#    - join: first time in
#    - leave: leave the system, and the group
#    - list_my_peers: who is in chatting with me?
#    - list_all: who is in the system, and the chat groups
#    - connect: connect to a peer in a chat group, and become part of the group
#    - disconnect: leave the chat group but stay in the system
# ==============================================================================


class Group:

    def __init__(self):
        self.members = {}
        self.chat_grps = {}
        self.grp_ever = 0

    def join(self, name):
        self.members[name] = S_ALONE
        return

    def is_member(self, name):

        if name in self.members.keys():
            return True
        else:
            return False

    def leave(self, name):
        self.disconnect(name)
        del self.members[name]

    def find_group(self, name):
        """
        Auxiliary function internal to the class; return two
        variables: whether "name" is in a group, and if true
        the key to its group
        """

        found = False
        group_key = 0
        if self.members[name] == S_ALONE:
            return found, group_key
        else:
            for key, group in self.chat_grps.items():
                if name in group:
                    found = True
                    group_key = key
                    break
            return found, group_key
                
        

    def connect(self, me, peer):
        """
        me is alone, connecting peer.
        if peer is in a group, join it
        otherwise, create a new group with you and your peer
        """
        peer_in_group, group_key = self.find_group(peer)

        if self.members[me] == S_TALKING:
            raise Exception("You are already in a group.")
        
        if not peer_in_group:
            self.grp_ever += 1
            self.chat_grps[self.grp_ever] = [me, peer]
            self.members[peer] = S_TALKING
        else:
            self.chat_grps[group_key].append(me)
        self.members[me] = S_TALKING
        return

    # implement
    def disconnect(self, me):
        if self.members[me] == S_ALONE:
            return
        for key, group in self.chat_grps.items():
            if me in group:
                group.remove(me)
            self.members[me] = S_ALONE
            if len(group) == 1:
                self.members[group[0]] = S_ALONE
                del self.chat_grps[key]
            break
        return
        



        
    def list_all(self):
        # a simple minded implementation
        full_list = "Users: ------------" + "\n"
        full_list += str(self.members) + "\n"
        full_list += "Groups: -----------" + "\n"
        full_list += str(self.chat_grps) + "\n"
        return full_list

    # implement
    def list_me(self, me):
        """
        return a list, "me" followed by other peers in my group
        """
        my_list = []
        my_list.append(me)
        my_group = None
        for group in self.chat_grps.values():
            if me in group:
                my_group = group
                break
        for member in my_group:
            if member != me:
                my_list.append(member)


        
        return my_list


if __name__ == "__main__":
    g = Group()
    g.join('a')
    g.join('b')
    g.join('c')
    g.join('d')
    print(g.list_all())

    g.connect('a', 'b')
    print(g.list_all())
    g.connect('c', 'a')
    print(g.list_all())
    g.leave('c')
    print(g.list_all())
    g.disconnect('b')
    print(g.list_all())
