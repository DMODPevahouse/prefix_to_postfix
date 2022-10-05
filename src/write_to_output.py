# ----- Script Creator
# ----- David Pevahouse
# ----- Date
# ----- 9/30/2022
# ----- Purpose ------
# Purpose of this method is to check if there are errors, and report the results
#
# ----- Description ------
# The function that calls this will depend on pre_to_postfix.py calling it
# then passing in variables that test for errors on what could happen
# incorrectly with the prefix expression. If there are no errors, then the
# correct postfix expression is reported. If there are errors, then the prefix
# is declared invalid, and the reason why it is invalid is reported.

from src.evaluate_postfix import evaluatePostfix


# Purpose of this def is to check for errors, report them, and if no errors,
# report the correct postfix expressions
def output_to_file(temp, isvalid, operator_exists, operand_exists, file1, prefix, solve_numbers):
    if operator_exists is False:
        file1.write("No operators in the equation, invalid: " + prefix + '\n\n')
    elif operand_exists is False:
        file1.write("No operands in the equation, invalid: " + prefix + '\n\n')
    elif temp is None:
        file1.write("No value given for the prefix, it is null" + "\n\n")
    elif not isvalid:
        file1.write("Invalid prefix expression:  " + prefix + "\n\n")
    else:
        file1.write("The prefix expression is: " + prefix + "\n")
        file1.write("The postfix expression is: " + temp + "\n")
        if solve_numbers is True:
            answer = evaluatePostfix(temp)
            file1.write("The answer is: " + str(answer) + "\n\n")
