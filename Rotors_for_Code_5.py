from Checkers_for_Code_5 import *
import copy


# _______________________________Rotors Class_______________________________
class rotor_from_name(Checkers):

    # ____________________________init__________________________________
    # It keeps all rotor config, argument is the name of the rotor
    # Variables:
    # name: Name of rotors
    # ring_set is at default position = A or 01 (No rotation)
    # position_set is at default position = A (No rotation)
    def __init__(self, name, ring_set="01", position_set=0, new_elements=[]):
        self.name = name
        # Active Checker
        self.new_name = self.rotor_checker(self.name)

        # All rotors config
        # Input
        self.__label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        # Rotors (Rotate)
        self.rotor_Beta = ['L', 'E', 'Y', 'J', 'V', 'C', 'N', 'I', 'X', 'W', 'P', 'B', 'Q', 'M', 'D', 'R', 'T', 'A',
                             'K', 'Z', 'G', 'F', 'U', 'H', 'O', 'S']
        self.rotor_Gamma = ['F', 'S', 'O', 'K', 'A', 'N', 'U', 'E', 'R', 'H', 'M', 'B', 'T', 'I', 'Y', 'C', 'W', 'L',
                              'Q', 'P', 'Z', 'X', 'V', 'G', 'J', 'D']
        self.rotor_I = ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S",
                          "P", "A", "I", "B", "R", "C", "J"]
        self.rotor_II = ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G",
                           "Z", "N", "P", "Y", "F", "V", "O", "E"]
        self.rotor_III = ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W",
                            "G", "A", "K", "M", "U", "S", "Q", "O"]
        self.rotor_IV = ["E", "S", "O", "V", "P", "Z", "J", "A", "Y", "Q", "U", "I", "R", "H", "X", "L", "N", "F",
                           "T", "G", "K", "D", "C", "M", "W", "B"]
        self.rotor_V = ["V", "Z", "B", "R", "G", "I", "T", "Y", "U", "P", "S", "D", "N", "H", "L", "X", "A", "W", "M",
                          "J", "Q", "O", "F", "E", "C", "K"]
        # reflectors (No rotate)
        self.rotor_A = ["E", "J", "M", "Z", "A", "L", "Y", "X", "V", "B", "W", "F", "C", "R", "Q", "U", "O", "N", "T",
                          "S", "P", "I", "K", "H", "G", "D"]
        self.rotor_B = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F',
                          'Z', 'C', 'W', 'V', 'J', 'A', 'T']
        self.rotor_C = ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X', 'W', 'G', 'C', 'T', 'K', 'U',
                          'Q', 'S', 'B', 'N', 'M', 'H', 'L']

        self.new_rotor = new_elements

        # If position_set == 0, means no rotation in the list
        if position_set == 0:
            position_set = "A"

        position_set = self.__position_setting(position_set)

        # Initialize tuples and rotation according to position setting
        self.rot_elements_init = self.__initialization(self.new_name, self.__label, position_set, ring_set)


    # ____________________________Initilization__________________________________
    # Initialize all rotors according to their position and ring settings
    # Variables:
    # input_list: It will always be __label
    # rot_spaces: Spaces to move based on position and ring settings
    # ring_set: To shift uo the list and move from left to right
    def __initialization(self, new_name, input_list, rot_spaces=0, ring_set="01", new_elements=[]):

        if new_name == "NEW":
            self.rotor_XXX = self.new_rotor
        if new_name == "BETA":
            self.rotor_XXX = self.rotor_Beta
        if new_name == "GAMMA":
            self.rotor_XXX = self.rotor_Gamma
        if new_name == "I":
            self.rotor_XXX = self.rotor_I
        if new_name == "II":
            self.rotor_XXX = self.rotor_II
        if new_name == "III":
            self.rotor_XXX = self.rotor_III
        if new_name == "IV":
            self.rotor_XXX = self.rotor_IV
        if new_name == "V":
            self.rotor_XXX = self.rotor_V

        # Reflector cannot rotate
        if new_name == "A":
            rot_spaces = 0
            self.rotor_XXX = self.rotor_A
        if new_name == "B":
            rot_spaces = 0
            self.rotor_XXX = self.rotor_B
        if new_name == "C":
            rot_spaces = 0
            self.rotor_XXX = self.rotor_C

        # Activate ring_setting to shift up the list and slide X value according to ring_set
        self.ring_matrix = self.__ring_setting(self.rotor_XXX, ring_set)

        # Tuple creation (__label,rotors)
        self.TUPLE = self.__tuples(input_list, self.ring_matrix)
        # Tuple Rotation if rot_spaces =! 0
        self.rot_elements = self.__rotating_elements(self.TUPLE, rot_spaces)
        return self.rot_elements


    # ____________________________Encode_right_to_left__________________________________
    # Swap characters according to rotor from input list (__label) to selected rotor
    # Variables:
    # char: string of length 1
    # element_index: element_index based on input list (__label) if a 0 value is
    # tuple_rotation: represents the rotation for key pressed or rotation with notches
    # init: To know if it´s the first rotor, false if it´s not
    def encode_right_to_left(self, char, element_index=0, tuple_rotation=0, init=True):

        #print(f"El rotor es: {self.name}")

        # Active checker to know if all parameters are good to continue
        self.new_char = self.checker(char, 1)
        #print(f"la letra ingresada es: {self.new_char}")

        # Rotation elements, if the a letter is inserted (tuple_rotation)
        self.rot_elements = self.__rotating_elements(self.rot_elements_init, tuple_rotation)

        # Active indices
        # 0 and true to know if this is the very first character inserted and avoid wrong returned values from other rotors
        if all((element_index == 0, init == True)):
            self.transfer_index = self.__indeces(self.new_char, self.__label)
        else:
            self.transfer_index = element_index

        # Transfering the index from input list to rot_elements list (tuple)
        self.rot_elements_tuple = self.rot_elements[self.transfer_index]
        #print(f"La tupla buscada es: {self.rot_elements_tuple}")

        # Saving rot_elements for future movements
        self.rot_elements = self.__saving_lists(self.rot_elements)

        # Return the values
        # Save character and index to transfer to next rotor

        #self.transfer_character, self.transfer_character_reverse, self.transfer_index = self.__indeces(self.rot_elements[1], self.rot_elements)
        # Return the values
        # transfer_character_reverse: from rotor to input list (__label)
        # transfer_character: from input list (__label) to rotor
        for i in range(len(self.rot_elements)):
            if self.rot_elements_tuple[1] == self.rot_elements[i][0]:
                #print(f"La letra en rotor es: {self.rot_elements[i][0]}")
                # Character in rotor
                self.transfer_character = self.rot_elements[i][0]
                # Character in input list (it´s only useful when encode_left_to_eigt method is call)
                self.transfer_character_reverse = self.rot_elements[i][1]
                # Input list index
                self.transfer_index = i
                #print(f"El indice en input list es: {self.transfer_index}")

        return self.transfer_character


    # ____________________________Indices__________________________________
    # Looking for the index in the list (right to left)
    def __indeces(self, char, list):
        # reading the alphabet
        for i in range(len(list)):
            if char == list[i]:
                self.index = list.index(char)
        return self.index


    # ____________________________encode_left_to_right__________________________________
    # Swap characters according to rotor from selected rotors to input list (__label)
    # Variables:
    # char: string of length 1
    # element_index: element_index based on selected rotor, 0 means no rotors were before of it
    # last_matrix: It represents the previous rotor matrix and 0 means no rotors were before of it (default last_matrix is __label)
    def encode_left_to_right(self, char, element_index = 0, last_matrix = 0):

        #print(f"El rotor es: {self.name}")

        # Active checker to know if all parameters are good to continue
        self.new_char = self.checker(char, 1)
        #print(f"la letra ingresada es: {self.new_char}")


        # Default matrix is __label
        if last_matrix == 0:
            last_matrix = self.__label

        # Active indices
        # 0 and 0 to know if this is the if only one character was inserted and avoid wrong returned values from other rotors
        # else to take the previous rotor´s index
        if all((element_index == 0, last_matrix ==0)):
            self.transfer_index = self.__indeces_reverse(self.new_char)
        else:
            self.transfer_index = element_index

        # Transfering the index from input list (__label) or previous rotor matrix to rot_elements list (tuple)
        self.rot_elements_tuple = last_matrix[self.transfer_index]
        #print(f"La tupla buscada es: {self.rot_elements_tuple}")

        # Saving rot_elements for future movements
        self.rot_elements = self.__saving_lists(self.rot_elements)

        # Return the values
        # Save character and index to transfer next rotor
        # transfer_charater: from rotor to input list (__label)
        # transfer_character_reverse: from input list (__label) to rotor
        for i in range(len(self.rot_elements)):
            if self.rot_elements_tuple[0] == self.rot_elements[i][1]:
                #print(f"La letra en rotor es: {self.rot_elements[i][1]}")
                # Character in input list (it´s only useful when encode_left_to_eigt method is call)
                self.transfer_character = self.rot_elements[i][1]
                self.transfer_character_reverse = self.rot_elements[i][0]
                self.transfer_index = i
                #print(f"El indice en input list es: {self.transfer_index}")
        return self.transfer_character_reverse


    # ____________________________Indices_reverse__________________________________
    # Looking for the index in the list (reverse mode)
    def __indeces_reverse(self, char):
        # reading the rotors
        for i in range(len(self.rot_elements)):
            if char == self.rot_elements[i]:
                self.index_rev = self.rot_elements.index(char)
        return self.index_rev


    # ____________________________Rotating elements__________________________________
    # To slide the elements in the list based on ring setting and position
    def __rotating_elements(self, list, spaces=0):

        # creating a new for rotors rotation
        self.new_list = list

        # Sliding the first element "n" spaces
        for n in range(0, spaces):
            self.new_list += [self.new_list.pop(0)]
        return self.new_list


    # ____________________________Tuples__________________________________
    # Creating tuples (Rotors)
    def __tuples(self, input_list, rotor_list):

        # creating tuples in list for rotors rotation
        self.tuple = list(zip(input_list, rotor_list))
        return self.tuple

    # ____________________________notches__________________________________
    # Definition of every rotor´s notches
    def notches(self, Activer = False):
        # Activer to know the state of the rotor:
        # "True" makes reference that the character has already passed
            # notch will be value of letter + 1. ie. if notch is B, the click will active on C
        # "False" makes reference that the character is still at the same position [0][0]
        clicks = 0
        # Rotor I notch must be Q
        if self.new_name == "I":
            if all(("R" == self.rot_elements[0][0], Activer == True)):
                clicks = 1
            if all(("Q" == self.rot_elements[0][0], Activer == False)):
                clicks = 1
        # Rotor II notch must be E
        if self.new_name == "II":
            if all(("F" == self.rot_elements[0][0], Activer == True)):
                clicks = 1
            if all(("E" == self.rot_elements[0][0], Activer == False)):
                clicks = 1
        # Rotor III notch must be V
        if self.new_name == "III":
            if all(("W" == self.rot_elements[0][0], Activer == True)):
                clicks = 1
            if all(("V" == self.rot_elements[0][0], Activer == False)):
                clicks = 1
        # nRotor IV otch must be J
        if self.new_name == "IV":
            if all(("K" == self.rot_elements[0][0], Activer == True)):
                clicks = 1
            if all(("J" == self.rot_elements[0][0], Activer == False)):
                clicks = 1
        # Rotor V notch must be Z
        if self.new_name == "V":
            if all(("A" == self.rot_elements[0][0], Activer == True)):
                clicks = 1
            if all(("Z" == self.rot_elements[0][0], Activer == False)):
                clicks = 1
        return clicks


    # ____________________________Saving_lists__________________________________
    # Saving the tuples for each rotor
    def __saving_lists(self, lists):
        # Coping th list
        self.new_list = copy.deepcopy(lists)
        return self.new_list


    # ____________________________Position_setting__________________________________
    # Defining Initial position for any rotor, based on position settings
    def __position_setting(self, position):

        # Active checkers to know if all is ok to continue
        self.position = self.checker(position, 1)

        # Transforming letters to numbers
        self.init_position = ord(self.position) - 65

        return self.init_position


    # ____________________________Ring_setting__________________________________
    # Defining Initial position for any rotor, based on rotor settings (shift up the list and moving from left to right)
    def __ring_setting(self, rotor_XXX, ring_set=0):
        # Active checkers to know if all is ok to continue
        self.ring = self.ring_setting_checker(ring_set)

        self.ring -= 1

        for i in range(len(rotor_XXX)):
            rotor_XXX[i] = ord(rotor_XXX[i]) + self.ring
            if rotor_XXX[i] >= 91:
                rotor_XXX[i] -= 26
        for j in range(len(rotor_XXX)):
            rotor_XXX[j] = chr(rotor_XXX[j])

        for k in range(0, self.ring):
            rotor_XXX.insert(0, rotor_XXX[-1])
            rotor_XXX.pop()

        return rotor_XXX
