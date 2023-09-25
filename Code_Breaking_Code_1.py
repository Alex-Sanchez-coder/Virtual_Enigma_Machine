from Pluglead_Plugboard import *
from Rotors import *
import time

##################################################################################################################################
###
### READ THIS:   THE PARAMETERS THAT NEED TO BE SET UP ARE THE GIVEN CONDITIONS THAT THE INSTRUCTIONS MENTIONED PLEASE GO TO THE BOTTOM TO SEE
### Rotors: Beta Gamma V and 0 value to not include a 4 rotor   (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### Reflector: The reflector was changing from Reflector A to C (THE CODE ITERATES THIS PART)
### Ring settings: 04 02 14 and 0 value to not include a 4 rotor    (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### Starting positions: MJM and 0 value to not include a 4 rotor    (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### Plugboard pairs: KI XN FL   (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### The code introduced was: DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### crib SECRETS (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### ALL PARAMETERS MUST BE STRING TYPE EXCEPT O VALUES FOR 4TH ROTOR, IT SHOULD BE INT TYPE
###
### NOTE: IF THE INPUTS DO NOT CHANGE, JUST RUN A THE RESULT WILL BE PRINTED
###
###################################################################################################################################


###################################################################################
###                                DO NOT MODIFY
###################################################################################

#___________________________________________Enigma Machine set up ___________________________________________________________________
# Parameters: LHS: Left Hand side & RHS: Right HAnd Side.
# RHS values are in 0 by default, that means the machine is configured to use 3 rotors and 1 reflector
# If any RHS value is set in 0, the simulator will use only 3 rotors + 1 reflector
# To switch to M4 enigma machine (4 rotors + 1 reflector), all RHS values must be filled
# Rotors:
# LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor
# Reflector: Reflector
# Ring settings:
# LHS_ring_setting, Middle_ring1_setting, Middle_ring2_setting, RHS_ring_setting
# Position settings:
# LHS_position_setting, Middle_position1_setting, Middle_position2_setting, RHS_position_setting
# letters: String to be encoded or decoded

def enigma_machine_set_up(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor = 0, Reflector = "", LHS_ring_setting = "", Middle_ring1_setting= "",
            Middle_ring2_setting="", RHS_ring_setting = 0, LHS_position_setting = "", Middle_position1_setting = "",
            Middle_position2_setting = "", RHS_position_setting = 0, letters = ""):

    check = Checkers()
    check.no_rep_rotors(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor, Reflector)

    # Variables:
    # Message: List where the message will appear
    # RHS_Click: Represents the rotation for every keypress and it stars with 1
    # Flag: To know if there are 3 (True) or 4 (False) rotors
    RHS_click = 1
    Message = []
    Flag = False

    # Defining parameters for 3 rotors + 1 reflector
    if RHS_rotor == 0 or RHS_ring_setting == 0 or RHS_position_setting == 0:
        RHS_rotor = Middle_rotor2
        RHS_ring_setting = Middle_ring2_setting
        RHS_position_setting = Middle_position2_setting
        Flag = True

    # Declaring all objects with all positions (3 Rotors + 1 Reflector)
    # Referencing to [def __init__(self, name, ring_set="01", position_set=0)]:
    rotor1 = rotor_from_name(RHS_rotor, RHS_ring_setting, RHS_position_setting)
    rotor25 = rotor_from_name(Middle_rotor2, Middle_ring2_setting, Middle_position2_setting)
    rotor3 = rotor_from_name(Middle_rotor1, Middle_ring1_setting, Middle_position1_setting)
    rotor4 = rotor_from_name(LHS_rotor, LHS_ring_setting, LHS_position_setting)
    reflector = rotor_from_name(Reflector)


    # Creating For loop to encrypt // decrypt the word(s)
    for i in range(len(letters)):

        # Swapping the letters according the plugboard_setup
        swap_init_letter = plugboard.encode(letters[i])

        # Referencing to method [encode_right_to_left(self, char, element_index = 0, tuple_rotation=0, init=True):]
        # Variables:
        # init: To know if it´s the first rotor
        # RHS_Click: Represents the rotation for every keypress
        rotor1.encode_right_to_left(swap_init_letter, 0, RHS_click)

        # Variables:
        # Middle_click1: To know if the notch passed in rotor 1 and "True" makes reference that the character has already passed
        # Middle_click2: To know if the notch passed in rotor 2 and "False" makes reference that the character is still at the same postion [0][0]
        # Last_click: To rotate the last rotor (3 rotors), 0 is only considering 4 rotors
        # Middle_click: Sum up previous variables to know if there was a double step process == 2 and rotate once the rotor 2
        Middle_click1 = rotor1.notches(True)

        # If 3 rotors were selected flag=True, then keep only one middle rotor instead of 2
        if Flag == True:

            Middle_click2 = rotor3.notches(False)
            Middle_click = Middle_click1 + Middle_click2
            if Middle_click >= 2:
                Middle_click = 1

            rotor3.encode_right_to_left(rotor1.transfer_character, rotor1.transfer_index, Middle_click, False)
            Last_click = Middle_click2

        else:

            Middle_click2 = rotor25.notches(False)
            Middle_click = Middle_click1 + Middle_click2
            if Middle_click >= 2:
                Middle_click = 1

            rotor25.encode_right_to_left(rotor1.transfer_character, rotor1.transfer_index, Middle_click, False)
            rotor3.encode_right_to_left(rotor25.transfer_character, rotor25.transfer_index, Middle_click2, False)
            Last_click = 0

        rotor4.encode_right_to_left(rotor3.transfer_character, rotor3.transfer_index, Last_click, False)

        reflector.encode_right_to_left(rotor4.transfer_character, rotor4.transfer_index, 0, False)

        # Referencing to method [def encode_left_to_right(self, char, element_index = 0, last_matrix = 0):]
        # Variables:
        # char: To know if it´s the first rotor
        # RHS_Click: Represents the rotation for every keypress
        rotor4.encode_left_to_right(reflector.transfer_character_reverse, reflector.transfer_index, rotor4.rot_elements)

        if Flag == True:

            rotor3.encode_left_to_right(rotor4.transfer_character, rotor4.transfer_index, rotor3.rot_elements)
            rotor1.encode_left_to_right(rotor3.transfer_character, rotor3.transfer_index, rotor1.rot_elements)

        else:

            rotor3.encode_left_to_right(rotor4.transfer_character, rotor4.transfer_index, rotor3.rot_elements)
            rotor25.encode_left_to_right(rotor3.transfer_character, rotor3.transfer_index, rotor25.rot_elements)
            rotor1.encode_left_to_right(rotor25.transfer_character, rotor25.transfer_index, rotor1.rot_elements)

        rotor1.encode_left_to_right(rotor1.transfer_character, rotor1.transfer_index)

        # Swapping the letters according the plugboard_list
        swap_end_letter = plugboard.encode(rotor1.transfer_character)

        Message.append(swap_end_letter)
    #print(Message)
    return Message


###################################################################################
###                                DO NOT MODIFY
###################################################################################

#___________________________________________Plugboard set up___________________________________________________________________
# To create plugboard based on the input
def plugboard_set_up(plugboard_string):

    if plugboard_string == "":
        pass

    else:
        # Creating a list based in the input string
        plugboard_list = plugboard_string.rsplit(" ")

        # Plugboard Set up
        for i in range(len(plugboard_list)):
            plugboard.add(PlugLead(plugboard_list[i]))

###################################################################################
###                                DO NOT MODIFY
###################################################################################

#___________________________________________decrypting___________________________________________________________________
def decrypting(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor, Reflector_list, LHS_ring_setting, Middle_ring1_setting,
            Middle_ring2_setting, RHS_ring_setting, LHS_position_setting, Middle_position1_setting,
            Middle_position2_setting, RHS_position_setting, encoded_message, crib):

    # Changing Reflectors until get the crib in the message
    for i in range(len(Reflector_list)):

        # Saving the result in a list
        encoded_message_proposal = enigma_machine_set_up(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor, Reflector_list[i], LHS_ring_setting, Middle_ring1_setting,
            Middle_ring2_setting, RHS_ring_setting, LHS_position_setting, Middle_position1_setting,
            Middle_position2_setting, RHS_position_setting, encoded_message)

        # Turning the encoded_message_proposal (list) into string to be compared with crib
        encoded_message_proposal_string = "".join(encoded_message_proposal)
        if crib in encoded_message_proposal_string:
            print(f"The reflector is: {Reflector_list[i]}")
            print(f"The original message is: {encoded_message_proposal_string}")
            #return Reflector_list[i], encoded_message_proposal_string



#___________________________________________Main___________________________________________________________________
# To measure the time in secs
start = time.time()

# creating the instance for Plugboard
plugboard = Plugboard()

# Insert here the plugboard_____________(DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
plugboard_set_up("KI XN FL")

#Insert here the encoded message_____________(DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
encoded_message = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"

# Do no change
Reflector_list = "ABC"

# Insert here the crib _____________(DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
crib = "SECRETS"
crib = crib.upper()

#Insert here enigma machine settings_____________(DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)

#Rotors:  (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
# If the machine is M3 (3 rotors + 1 Reflector), set all RHS values in 0
# "Beta", "Gamma", "V", 0, Reflector_list[i], "04", "02", "14", 0, "M", "J", "M",
LHS_rotor = "Beta"
Middle_rotor1 = "Gamma"
Middle_rotor2 = "V"
RHS_rotor = 0

# Ring settings: (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
LHS_ring_setting = "04"
Middle_ring1_setting = "02"
Middle_ring2_setting = "14"
RHS_ring_setting = 0

# Position settings: (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
LHS_position_setting = "M"
Middle_position1_setting = "J"
Middle_position2_setting = "M"
RHS_position_setting = 0

# Function to iterate and find the answers
decrypting(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor, Reflector_list, LHS_ring_setting, Middle_ring1_setting,
            Middle_ring2_setting, RHS_ring_setting, LHS_position_setting, Middle_position1_setting,
            Middle_position2_setting, RHS_position_setting, encoded_message, crib)
print("\nAll combinations were explored.")
end = time.time()
print(f"The execution time was:  {end-start} secs")