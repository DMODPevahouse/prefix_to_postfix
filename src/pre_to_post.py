# ----- Script Creator
# ----- David Pevahouse
# ----- Date
# ----- 9/30/2022
# ----- Purpose ------
# The purpose of this module is to hold the class that will actually transform
# the prefix equation to a postfix equation
#
# ----- Description ------
# This class will use stack functionality to read in and analyze prefix equations
# and transform them to postfix equations. It will create a stack and continually
# pop and push as error checking and proper usage of operands and operators allows
# We will have a separate function to check to make sure that what is read is correct
# and if not, will error out. To do so there will be multiple variables keeping track
# of if an equation is true or false based on what has happened in the stack
# keeping track of improper usage of a prefix equation

from src.stack_node import Stack
from src.write_to_output import output_to_file

class PreToPost:
    # This function checks if the character is an operator
    def is_operator(self, text):
        if text == "+" or text == "-" or text == "*" or text == "/" or text == "$" or text == "%" or text == "<" or text == ">":
            return True
        else:
            return False
    # This function checks if it is an operand
    def is_operand(self, text):
        if ("0" <= text <= "9") or ("a" <= text <= "z") or ("A" <= text <= "Z") or text == "<" or text == ">":
            return True
        else:
            return False

    def is_operand_number(self, text):
        if "0" <= text <= "9":
            return True
        else:
            return False

    def is_operand_letter(self, text):
        if "a" <= str(text) <= "z" or "A" <= str(text) <= "Z":
            return True
        else:
            return False

    def prefix_to_postfix(self, prefix, output):
        size = len(prefix)
        s = Stack()
        combo = ""
        operation1 = ""
        operation2 = ""
        isvalid = True
        i = size - 1
        operator_exists = False
        operand_exists = False
        is_numbers = False
        is_letters = False
        solve_numbers = False
        file1 = open(output, "a")
        while i >= 0:
            # Makes sure there is enough operands to perform the operator on
            # then performs the push in order to get the proper form ready
            if self.is_operator(prefix[i]) and prefix[i] != "<" and prefix[i] != ">":
                operator_exists = True
                if s.size() > 1:
                    operation1 = s.pop()
                    operation2 = s.pop()
                    combo = operation1 + operation2 + prefix[i]
                    s.push(combo)
                else:
                    isvalid = False
            # pushes to the stack if it is an operand
            elif self.is_operand(prefix[i]):
                # this section will combine two numbers to allow for double
                # digit, or more, operands to be used in the postfix equation
                if prefix[i] == ">":
                    j = i
                    j -= 1
                    multi = ""
                    digit_counter = 1
                    first = 1
                    s.push(multi)
                    while prefix[j] != "<" or j >= 0:
                        if prefix[j] == ">":
                            isvalid = False
                            file1.write("Invalid use of <>" + "\n")
                        elif prefix[j] == "<":
                            if digit_counter > 1:
                                while digit_counter > 1:
                                    temp1 = s.pop()
                                    if digit_counter == first:
                                        temp1 = "<" + temp1
                                    temp2 = s.pop()
                                    multi = temp1 + temp2
                                    if digit_counter == 2:
                                        multi = multi + ">"
                                    s.push(multi)
                                    digit_counter -= 1
                            break
                        else:
                            s.push(prefix[j])
                            digit_counter += 1
                            first += 1
                            j -= 1
                    i = j
                else:
                    s.push(prefix[i])
                operand_exists = True
                if self.is_operand_number(prefix[i]):
                    is_numbers = True
                if self.is_operand_letter(prefix[i]) and prefix[i] != ">" and prefix[i] != "<":
                    is_letters = True
            # this will look for white spaces in the equation, if it happens to be
            # at the beginning of the line or the end, it will ignore it, but if it
            # is in the middle, it will error out, as it should be 1 prefix per line
            elif prefix[i] == " ":
                if self.is_operator(prefix[i + 1]) or self.is_operand(prefix[i + 1]):
                    if self.is_operator(prefix[i - 1]) or self.is_operand(prefix[i - 1]):
                        file1.write("Invalid, please only have one prefix per line:  ")
                        isvalid = False
                    else:
                        pass
            elif prefix[i] == "\n":  # ignore new lines should it exist
                pass
            elif prefix[i] == "\r":  # ignore windows return should it exist
                pass
            else:
                isvalid = False
            i -= 1
        else:
            # display correct result by sending it to another function that
            # will error check the results to make sure to print helpful
            # messages about what is going on
            temp = s.pop()
            if is_numbers is True and is_letters is False:
                solve_numbers = True
            output_to_file(temp, isvalid, operator_exists, operand_exists, file1, prefix, solve_numbers)
        if s.is_empty() is False:
            s.empty_stack()
        file1.close()

