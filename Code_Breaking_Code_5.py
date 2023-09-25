from Pluglead_Plugboard import *
from Rotors_for_Code_5 import *
import time
import itertools

##################################################################################################################################
###
### READ THIS:   THE PARAMETERS THAT NEED TO BE SET UP ARE THE GIVEN CONDITIONS THAT THE INSTRUCTIONS MENTIONED PLEASE GO TO THE BOTTOM TO SEE
### Rotors: V II IV and 0 value to not include a 4 rotor   (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### Reflector: UNKNOWN, a standard reflector whith a variation in 8 pairs (THIS PART IS ITERATED BY THE CODE)
### Ring settings: 06 18 07 and 0 value to not include a 4 rotor    (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### Starting positions: AJL and 0 value to not include a 4 rotor    (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### Plugboard pairs: UG IE PO NX WT (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### The code introduced was: HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
### crib UNKNOWN (POSSIBLE LIST WILL BE A SOCIAL MEDIA: )
###
###################################################################################################################################




#___________________________________________Enigma Machine set up (DO NOT MODIFY)___________________________________________________________________
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

# ___________________________________________Enigma Machine set up (DO NOT MODIFY)___________________________________________________________________
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

def enigma_machine_set_up(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor=0, Reflector="", LHS_ring_setting="",
                          Middle_ring1_setting="",
                          Middle_ring2_setting="", RHS_ring_setting=0, LHS_position_setting="",
                          Middle_position1_setting="",
                          Middle_position2_setting="", RHS_position_setting=0, letters="", new_elements=[]):
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
    reflector = rotor_from_name(Reflector, new_elements=new_elements)

    # Creating For loop to encrypt // decrypt the word(s)
    for i in range(len(letters)):
        # print(letters[i])

        # print(rotor1.rot_elements)
        # print(rotor25.rot_elements)
        # print(rotor3.rot_elements)
        # print(rotor4.rot_elements)

        # Referencing to method [encode_right_to_left(self, char, element_index = 0, tuple_rotation=0, init=True):]
        # Variables:
        # init: To know if it´s the first rotor
        # RHS_Click: Represents the rotation for every keypress
        rotor1.encode_right_to_left(letters[i], 0, RHS_click)

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

        # print(rotor1.rot_elements)
        # print(rotor25.rot_elements)
        # print(rotor3.rot_elements)
        # print(rotor4.rot_elements)

        Message.append(rotor1.transfer_character)
    # print(Message)
    return Message


# ___________________________________________Plugboard set up (DO NOT MODIFY)___________________________________________________________________
def plugboard_set_up(plugboard_string):
    if plugboard_string == "":
        pass

    else:
        # Creating a list based in the input string
        plugboard_list = plugboard_string.rsplit(" ")

        # Plugboard Set up
        for i in range(len(plugboard_list)):
            plugboard.add(PlugLead(plugboard_list[i]))


# ___________________________________________reset (DO NOT MODIFY)_______________________________________________________________
def reset():
    reset_list = [("A", ["E", "J", "M", "Z", "A", "L", "Y", "X", "V", "B", "W", "F", "C", "R", "Q", "U", "O", "N", "T",
                         "S", "P", "I", "K", "H", "G", "D"]),
                  ("B", ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F',
                         'Z', 'C', 'W', 'V', 'J', 'A', 'T']),
                  ("C", ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X', 'W', 'G', 'C', 'T', 'K', 'U',
                         'Q', 'S', 'B', 'N', 'M', 'H', 'L'])]
    return reset_list


# ___________________________________________comparing (DO NOT MODIFY)_______________________________________________________________

def comparing(encoded_message_proposal_string, crib, Reflector_list, elements, count):
    for m in range(len(crib)):
        if crib[m] in encoded_message_proposal_string:
            if Reflector_list == "A":
                print(f"The reflector variant is: A")
            elif Reflector_list == "B":
                print(f"The reflector variant is: B")
            elif Reflector_list == "C":
                print(f"The reflector variant is: C")

            print(f"the iteration was: {count}")
            print(f"The elements in the reflector are: {elements}")
            print(f"The original message is: {encoded_message_proposal_string}")
    return None


# ___________________________________________decrypting (DO NOT MODIFY)___________________________________________________________________
def decrypting(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor, Reflector_name, LHS_ring_setting,
               Middle_ring1_setting,
               Middle_ring2_setting, RHS_ring_setting, LHS_position_setting, Middle_position1_setting,
               Middle_position2_setting, RHS_position_setting, encoded_message, crib):
    Reflector_list = [
        ("A", ["E", "J", "M", "Z", "A", "L", "Y", "X", "V", "B", "W", "F", "C", "R", "Q", "U", "O", "N", "T",
               "S", "P", "I", "K", "H", "G", "D"]),
        ("B", ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F',
               'Z', 'C', 'W', 'V', 'J', 'A', 'T']),
        ("C", ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X', 'W', 'G', 'C', 'T', 'K', 'U',
               'Q', 'S', 'B', 'N', 'M', 'H', 'L'])]

    count = 0
    for r in range(len(Reflector_list)):

        for j in range(len(Reflector_list[r][1]) - 1):

            for i in range(len(Reflector_list[r][1]) - 3):
                #########################################################################################

                #########################################################################################

                # cambio separado cada
                Reflector_list[r][1][j], Reflector_list[r][1][j + 1], Reflector_list[r][1][i + 2], Reflector_list[r][1][
                    i + 3] = Reflector_list[r][1][j + 1], Reflector_list[r][1][j], Reflector_list[r][1][i + 3], \
                             Reflector_list[r][1][i + 2]

                # Reflector_list[r][1][i],Reflector_list[r][1][i+1],Reflector_list[r][1][i+2],Reflector_list[r][1][i+3]=Reflector_list[r][1][i+1],Reflector_list[r][1][i],Reflector_list[r][1][i+3],Reflector_list[r][1][i+2]

                # Running enigma machine
                # Saving the result in a list
                encoded_message_proposal = enigma_machine_set_up(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor,
                                                                 Reflector_name,
                                                                 LHS_ring_setting, Middle_ring1_setting,
                                                                 Middle_ring2_setting, RHS_ring_setting,
                                                                 LHS_position_setting, Middle_position1_setting,
                                                                 Middle_position2_setting, RHS_position_setting,
                                                                 encoded_message, Reflector_list[r][1])
                # print(encoded_message_proposal)

                # Turning the encoded_message_proposal (list) into string to be compared with crib
                encoded_message_proposal_string = "".join(encoded_message_proposal)
                # print(f"response1: {encoded_message_proposal_string}")
                encoded_message_proposal_string = comparing(encoded_message_proposal_string, crib, Reflector_list[r][0],
                                                            Reflector_list[r][1], count)
                count += 1
                print(count)
                Reflector_list = reset()

                #########################################################################################

                #########################################################################################

                # Cambio letras juntas caso 2
                Reflector_list[r][1][j], Reflector_list[r][1][j + 1], Reflector_list[r][1][i + 2], Reflector_list[r][1][
                    i + 3] = Reflector_list[r][1][i + 2], Reflector_list[r][1][i + 3], Reflector_list[r][1][j], \
                             Reflector_list[r][1][j + 1]

                # Reflector_list[r][1][i],Reflector_list[r][1][i+1],Reflector_list[r][1][i+2],Reflector_list[r][1][i+3]=Reflector_list[r][1][i+2],Reflector_list[r][1][i+3],Reflector_list[r][1][i],Reflector_list[r][1][i+1]

                # Running enigma machine
                # Saving the result in a list
                encoded_message_proposal = enigma_machine_set_up(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor,
                                                                 Reflector_name,
                                                                 LHS_ring_setting, Middle_ring1_setting,
                                                                 Middle_ring2_setting, RHS_ring_setting,
                                                                 LHS_position_setting, Middle_position1_setting,
                                                                 Middle_position2_setting, RHS_position_setting,
                                                                 encoded_message, Reflector_list[r][1])
                # print(encoded_message_proposal)

                # Turning the encoded_message_proposal (list) into string to be compared with crib
                encoded_message_proposal_string = "".join(encoded_message_proposal)
                # print(f"response1: {encoded_message_proposal_string}")
                encoded_message_proposal_string = comparing(encoded_message_proposal_string, crib, Reflector_list[r][0],
                                                            Reflector_list[r][1], count)
                count += 1
                print(count)
                Reflector_list = reset()

                #########################################################################################

                #########################################################################################

                Reflector_list[r][1][j + 1], Reflector_list[r][1][i + 2], Reflector_list[r][1][j], Reflector_list[r][1][
                    i + 3] = Reflector_list[r][1][i + 2], Reflector_list[r][1][j + 1], Reflector_list[r][1][i + 3], \
                             Reflector_list[r][1][j]

                # Reflector_list[r][1][i+1],Reflector_list[r][1][i+2],Reflector_list[r][1][i],Reflector_list[r][1][i+3] = Reflector_list[r][1][i+2],Reflector_list[r][1][i+1],Reflector_list[r][1][i+3],Reflector_list[r][1][i]

                # Running enigma machine
                # Saving the result in a list
                encoded_message_proposal = enigma_machine_set_up(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor,
                                                                 Reflector_name,
                                                                 LHS_ring_setting, Middle_ring1_setting,
                                                                 Middle_ring2_setting, RHS_ring_setting,
                                                                 LHS_position_setting, Middle_position1_setting,
                                                                 Middle_position2_setting, RHS_position_setting,
                                                                 encoded_message, Reflector_list[r][1])
                # print(encoded_message_proposal)

                # Turning the encoded_message_proposal (list) into string to be compared with crib
                encoded_message_proposal_string = "".join(encoded_message_proposal)
                # print(f"response1: {encoded_message_proposal_string}")
                encoded_message_proposal_string = comparing(encoded_message_proposal_string, crib, Reflector_list[r][0],
                                                            Reflector_list[r][1], count)
                count += 1
                print(count)
                Reflector_list = reset()


# ___________________________________________Main___________________________________________________________________
# To measure the time in secs
start = time.time()

# creating the instance for Plugboard
plugboard = Plugboard()

# Insert here the plugboard_____________(DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
plugboard_set_up("UG IE PO NX WT")

# Insert here the encoded message_____________(DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
encoded_message = "HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX"

# Do no change
Reflector_name = "new"

# Insert here the crib _____________(DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
crib = ["WWW", "FACEBOOK", "INSTAGRAM", "WHATSAPP", "SNAPCHAT", "TWITTER", "LINKEDIN", "PINTEREST", "TUMBLR", "REDDIT",
        "TIKTOK", "VIMEO", "COM"]
for i in range(len(crib)):
    crib[i] = crib[i].upper()

# Insert here enigma machine settings_____________(DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)

# Rotors:  (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
# If the machine is M3 (3 rotors + 1 Reflector), set all RHS values in 0
# "V", "III", "IV", 0, Reflector_list=A, "24", "12", "10", 0, "S", "W", "U", 0
LHS_rotor = "V"
Middle_rotor1 = "II"
Middle_rotor2 = "IV"
RHS_rotor = 0

# Ring settings: (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
LHS_ring_setting = "06"
Middle_ring1_setting = "18"
Middle_ring2_setting = "07"
RHS_ring_setting = 0

# Position settings: (DO NOT MODIFY ONLY IF THE SET UP IS DIFFERENT)
LHS_position_setting = "A"
Middle_position1_setting = "J"
Middle_position2_setting = "L"
RHS_position_setting = 0

decrypting(LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor, Reflector_name, LHS_ring_setting, Middle_ring1_setting,
           Middle_ring2_setting, RHS_ring_setting, LHS_position_setting, Middle_position1_setting,
           Middle_position2_setting, RHS_position_setting, encoded_message, crib)
end = time.time()
print(f"The execution time was:  {end - start} secs")