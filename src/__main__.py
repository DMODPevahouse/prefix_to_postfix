# ----- Script Creator
# ----- David Pevahouse
# ----- Date
# ----- 9/30/2022
# ----- Purpose ------
# The purpose of main is to set up the function, and call it
#
#
# ----- Description ------
# We do this by reading in the argument of the commandline to handle what the input
# and output files are. Then we call the function that will handle the rest of the
# program. We will report the success, or lack therof, of the program to the user
# by printing to the output file.


# from src import pre_to_post within function
from src.pre_to_post import PreToPost
# Helps read in filepaths
from pathlib import Path
# Imported to read argument from command line
import argparse
# Only imported to report back how long it took the function to run
import time

# when the function starts
start_time = time.time()

# Setting up the function
task = PreToPost()

# Using argparse to read in command line arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
args = arg_parser.parse_args()

in_file = Path(args.in_file)
output = Path(args.out_file)

# opening the input file, encoding to handle special characters
prefix_file = open(in_file, "r", encoding='ascii', errors='ignore')

# Count for how many prefix's have been tested
expression_count = 0
# Creates the output file
with open(output, 'w') as new_file:
    pass
# Opens the output file, runs the prefix to postfix function, and writes the
# results to the output file
for line in prefix_file:
    expression_file = open(output, 'a')
    expression_file.write("File line for the above attempted transformation: " + str(expression_count) + "\n\n")
    expression_count += 1
    task.prefix_to_postfix(line, output)
    expression_file.close()
# determines how long the function took to run, opening the file
# reporting the runtime by writing to the file, then closing the file
end_time = time.time()
execution_time = end_time - start_time
output_file = open(output, 'a')
output_file.write("Time it took to execute: " + str(execution_time) + "\n\n")
output_file.close()
