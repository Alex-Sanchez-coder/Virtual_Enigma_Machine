#_______________________________Class Checkers_______________________________
# This class controls and check if the parameters inserted in enigma machine are valid, if they are, the process continues, otherwise
# it provides to you a message with the issue.
class Checkers:
    # Message for errors in inputs
    # _______________________________Error Type_______________________________
    no_str_message = TypeError("Invalid Argument, the input must an alphabetical string")
    no_str_message1 = TypeError("Invalid Argument, the input must an alphabetical string")
    no_str_message2 = TypeError("Invalid Argument, the input must an alphabetical string of length 2")
    rep_message = TypeError("The second character must be different")
    short_long_message = TypeError("The string length is too short or long")
    full_list = ValueError("No more elements are accepted, Max.=10")
    no_in_the_list_rotor = ValueError("The argument is not in the list, please use Beta, Gamma, I, II, III, IV or V rotors")
    no_in_the_list_ring = ValueError("The argument is not in the list, please use string values from 01 up to 26")
    rotor_errors_message = ValueError("There must be at least 3 valid rotors")
    rotors_equal = ValueError("All rotors selected must be different")
    reflector_no_in_list = ValueError("Reflector is not in the list, please use A, B or C as a reflector")

    def __messages(self, *args):
        self.no_str_message = no_str_message
        self.no_str_message1 = no_str_message1
        self.no_str_message2 = no_str_message2
        self.short_long_message = short_long_message
        self.rep_message = rep_message
        self.full_list = full_list
        self.no_in_the_list_rotor = no_in_the_list_rotor
        self.no_in_the_list_ring = no_in_the_list_ring
        self.rotor_errors_message = rotor_errors_message
        self.rotors_equal = rotors_equal
        self.reflector_no_in_list = reflector_no_in_list

    # _______________________________checker_______________________________
    # Check if all parameters are ok
    def checker(self,string,length):

        # Checking length & if variable is string
        if type(string) == str:

            # All characters are now uppercase
            string=string.upper()

            # Unique If statement to check length = 1 for encode() method
            if all((length == 1, len(string) == length)):
                if all((string >= "A", string <= "Z")):
                    return string

                else:
                    raise self.no_str_message1

            # Unique if statement to check length = 2 for leads __init__
            elif all((length == 2, len(string) == length)):

                # Not duplicated characters
                if string[0] == string[-1]:
                    raise self.rep_message

                # Checking if two indexes are in the alphabet
                elif all((string[0] >= "A", string[0] <= "Z", string[1] >= "A", string[1] <= "Z")):
                    return string

                else:
                    raise self.no_str_message2

            else:
                raise self.short_long_message
        else:
            raise self.no_str_message


    # _______________________________check_plugboard_______________________________
    # Verifying if the character is already in the list
    def check_plugboard(self, list_lead, pair):
        for i in range(len(list_lead)):
            for j in range(0,2):
                if pair[j] in list_lead[i]:
                    raise ValueError(f"The element {pair[j]} in the argument is already plugged")


    # _______________________________Rotor_Checker_______________________________
    # Check if all parameters are ok
    def rotor_checker(self,string):
        self.__rotor_list=["BETA", "GAMMA", "I", "II", "III", "IV", "V", "A", "B", "C"]

        # Checking if variable is string
        if type(string) == str:

            # All characters are now uppercase
            string = string.upper()

            # Checking if string is in the list
            if string in self.__rotor_list:
                return string
            else:
                raise self.no_in_the_list_rotor
        else:
            raise self.no_str_message

    # _______________________________ring_setting_checker_______________________________
    # Check if the ring values are valid from 01 to 26
    def ring_setting_checker(self, string):
        self.__ring_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

        # Checking if variable is string
        if type(string) == str:

            # Checking if string is in the list
            if string in self.__ring_list:
                ring_values = [i for i in range (1,27)]
                ring_values_list = list(zip(self.__ring_list, ring_values))

                for j in range (0,26):
                    if string == ring_values_list[j][0]:
                        return ring_values_list[j][1]
            else:
                raise self.no_in_the_list_ring
        else:
            raise self.no_str_message


    # _______________________________no_rep_rotors_______________________________
    ## Avoiding to have more than once a rotor
    def no_rep_rotors(self,LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor, Reflector):
        rotor_list = [LHS_rotor, Middle_rotor1, Middle_rotor2, RHS_rotor]
        new_rotor_list=[]
        Reflector = self.reflectors_checker(Reflector)

        for i in range(len(rotor_list)):
            new_list = self.rotor_checker_init(rotor_list[i])
            new_rotor_list.append(new_list)


        LHS_rotor_count = new_rotor_list.count(new_rotor_list[0])
        Middle_rotor1_count = new_rotor_list.count(new_rotor_list[1])
        Middle_rotor2_count = new_rotor_list.count(new_rotor_list[2])
        RHS_rotor_count = new_rotor_list.count(new_rotor_list[3])

        if all((LHS_rotor_count == 1, Middle_rotor1_count == 1, Middle_rotor2_count == 1,  RHS_rotor_count == 1)):
            pass

        else:
            raise self.rotors_equal

    def rotor_checker_init(self,string):
        self.__rotor_list=["BETA", "GAMMA", "I", "II", "III", "IV", "V"]

        # Checking if variable is string
        if type(string) == str:

            # All characters are now uppercase
            string = string.upper()

            # Checking if string is in the list
            if string in self.__rotor_list:
                return string
            else:
                raise self.no_in_the_list_rotor

        elif string == 0:
            return 0

    # _______________________________reflectors_Checker_______________________________
    # Check if the reflector is valid
    def reflectors_checker(self,string):

        self.__reflector_list = ["A", "B", "C"]

        # Checking if variable is string
        if type(string) == str:

            # All characters are now uppercase
            string = string.upper()

            # Checking if string is in the list
            if string in self.__reflector_list:
                return string
            else:
                raise self.reflector_no_in_list
        else:
            raise self.no_str_message