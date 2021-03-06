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

        # IMPLEMENTATION
        # ---- start your code ---- #
        if name in self.members:
            return True
        return False
        # ---- end of your code --- #

    # implement
    def leave(self, name):
        """
        leave the system, and the group
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        self.disconnect(name)
        del self.members[name]
        # ---- end of your code --- #
        return

    def find_group(self, name):
        """
        Auxiliary function internal to the class; return two
        variables: whether "name" is in a group, and if true
        the key to its group
        """

        found = False
        group_key = 0
        # IMPLEMENTATION
        # ---- start your code ---- #
        if name in self.members:
            for k,v in self.chat_grps.items():
                if name in v:
                    found = True
                    group_key = k

        # ---- end of your code --- #
        return found, group_key

    def connect(self, me, peer):
        """
        me is alone, connecting peer.
        if peer is in a group, join it
        otherwise, create a new group with you and your peer
        """
        peer_in_group, group_key = self.find_group(peer)

        # IMPLEMENTATION
        # ---- start your code ---- #
        is_in_me_sys = self.is_member(me)
        is_in_peer_sys = self.is_member(peer)
        if is_in_me_sys and is_in_peer_sys:
            is_in_peer_grp, group_id_peer = self.find_group(peer)
            is_in_me_grp,group_id_me = self.find_group(me)
            self.members[me] = S_TALKING
            if not is_in_me_grp and not is_in_peer_grp:
                self.members[peer] = S_TALKING
                self.chat_grps[self.grp_ever+1] = []
                self.chat_grps[self.grp_ever+1].append(me)
                self.chat_grps[self.grp_ever+1].append(peer)
                self.grp_ever += 1
            if not is_in_me_grp and is_in_peer_grp:
                self.chat_grps[group_id_peer].append(me)

        # ---- end of your code --- #
        return

    # implement
    def disconnect(self, me):
        """
        find myself in the group, quit, but stay in the system
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        is_in = self.is_member(me)
        if is_in:
            is_in_group,group_id = self.find_group(me)
            if is_in_group:
                self.members[me] = S_ALONE
                self.chat_grps[group_id].remove(me)
                if len(self.chat_grps[group_id]) == 1:
                    the_other = self.chat_grps[group_id][0]
                    self.members[the_other] = S_ALONE
                    del self.chat_grps[group_id]
                elif len(self.chat_grps[group_id]) == 0:
                    del self.chat_grps[group_id]


        # ---- end of your code --- #
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
        # IMPLEMENTATION
        # ---- start your code ---- #
        is_in = self.is_member(me)
        if is_in:
            is_in_group, group_id = self.find_group(me)
            if is_in_group:
                my_list.append(me)
                for member in self.chat_grps[group_id]:
                    if member is not me:
                        my_list.append(member)

        # ---- end of your code --- #
        return my_list


    #Altenative implementation
    # def loners_num(self):
    #     pass
    #
    #
    # def biggest_grp(self):
    #     pass
    #
    #
    # def grps_two(self):
    #     pass


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
