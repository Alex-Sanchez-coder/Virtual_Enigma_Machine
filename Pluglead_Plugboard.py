
from Checkers import *

#_______________________________PlugLead Class_______________________________
class PlugLead(Checkers):

    #______________________________init__constructor__________________________________
    # Read the string
    def __init__(self, mapping):
        self.mapping = mapping
        # Active Checker
        self.new_mapping = self.checker(self.mapping,2)


    # ______________________________str__constructor__________________________________
    # To return the str value of __init__
    def __str__(self):
        return self.new_mapping


    # ____________________________encode string for pluglead_________________________________
    # To return / swap characters already inserted
    def encode(self, character):

        # Active checker
        self.new_character = self.checker(character, 1)

        # Checking if the character was inserted to return its couple, else return same character
        if self.new_character in self.new_mapping:
            if self.new_character == self.new_mapping[0]:
                return self.new_mapping[1]
            else:
                return self.new_mapping[0]
        else:
            return self.new_character


#_______________________________Plug Board Class_______________________________
class Plugboard(PlugLead):

    # ____________________________init__constructor________________________________
    # Variables:
    # self.count: to keep tracked list_lead and .add()
    # self.mark: For encode method purposes and to know if the character is not in the list
    # or the list has one element, returning the inserted character (Flag = 1)
    # self.list_lead: To list and save all plug leads Max = 10 (self.count)
    def __init__(self):
        self.count = 0
        self.mark = 0
        self.list_lead = []


    # ____________________________empty________________________________
    # To know if the list_lead is empty (self.count=0)
    def __empty(self):
        if self.count == 0:
            return True
        else:
            return False

    # ____________________________delete_all__________________________________
    # delete all method to delete everything in the list
    def delete_all(self):

        if self.__empty() == False:
            for i in range(0, self.count):
                self.list_lead.pop()
                self.count = 0

    # ____________________________add__________________________________
    # add method insert a new lead until list_lead has no more than 10 values
    def add(self, pair):
        # Converting to string value
        pair = str(pair)

        # Every time this method is succesfully call self.count increases by 1
        self.count += 1

        if self.__empty():
            self.list_lead.append(pair)

        elif self.count > 10:
            raise self.full_list

        # Verifying if the character is already in the list
        else:
            if self.check_plugboard(self.list_lead, pair):
                pass
            else:
                self.list_lead.append(pair)


    # ____________________________encode string for plugboard__________________________________
    # To return / swap characters already inserted along list_lead
    def encode(self, character):

        # Active checker
        self.new_character = self.checker(character, 1)

        # Checking if the character is in list_lead to return its couple, else return the character inserted
        for i in range(len(self.list_lead)):
            # If the character is in the list, swap and return the linked character, verifying both index position [0] or [1]
            if self.new_character in self.list_lead[i]:
                if self.new_character == self.list_lead[i][0]:
                    return self.list_lead[i][1]
                else:
                    return self.list_lead[i][0]

        return self.new_character

"""
#_______________________________MAIN_______________________________

if __name__ == "__main__":

    ### PLUGLEAD WORKS_________________________________
    #lead = PlugLead("ab")
    #print(lead.encode("b"))
    #lead = PlugLead("ah")
    #print(lead.encode("a"))

    ### PLUGBOARD WORKS________________________________
    plugboard = Plugboard()

    plugboard.add(PlugLead("ab"))
    plugboard.add(PlugLead("ef"))
    plugboard.add(PlugLead("gh"))
    plugboard.add(PlugLead("ij"))
    plugboard.add(PlugLead("kl"))
    plugboard.add(PlugLead("mn"))
    plugboard.add(PlugLead("op"))
    plugboard.add(PlugLead("qr"))
    plugboard.add(PlugLead("st"))
    plugboard.add(PlugLead("uV"))
    print(plugboard.list_lead)

"""