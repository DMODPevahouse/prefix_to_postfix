# Prefix to postfix

## Description
This lab was focused on making sure we can use stacks appropriately, without using libraries
that would create them for us. We were also tasked with creating a program that would take in
a prefix expression and convert it to postfix. The input and output needed the capability
to be read in from the arguments to support faster testing. This readme will go over how to
correctly use the lab. 

## Running the program

> Note: This program was written in Python 3.9.13
> Note: This program was written in Pycharm 2022.2.1
> Results may vary if you are using a different version of Python or Pycharm
> The source code can be found in the src folder

1. Download and install Python on your computer
2. Open up a terminal
3. Navigate to the directory containing the README.md
4. Run the program as a module: `python -m src -h`. This will print the help message.
5. Run the program as a module (with real inputs): `python -m src <some_input_file> <some_output_file>`
   a. IE: `python3 -m such \yourdirectoryhere\inputs\many_lines_input.txt D:\John_Hopkins_AI\data_structures\outputs\output.txt`

## usage:

```commandline
usage: python -m src in_file out_file

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname
```

## Sample Input and Output

There is a list of sample inputs in the directory inputs within the project, resting in the inputs directory:
 IE: D:\this_is\your_directory_path\here\inputs\input.txt


As for outputs, any output file will be created in the directory outputs within the project
and you will be able to name it whatever you want, the program will create it, resting in the output directory:
 

IE: \yourdirectoryhere\outputs\output.txt


When using the function you will need to use the full path to the input and output files
in order for it to be recognized

## Acceptable Input

The input file must be a text file with the prefix expression on each line. The input file
path must be given fully in order for the program to recognize it. The output file path
must be given fully in order for the program to recognize it. 
Acceptable input examples can include upper case, lower case, numbers, and symbols.
There is also some additional functionality. 
If you use single digits (0-9) in your input file, the program will solve the postfix 
expression and print the result to the output file.

If you wrap operands around with <> around it, the program will be able to take that in
as a single digit and report it back to. 

If there is an incorrect prefix expression, the program will print an error message to the output file.

If there is strange symbols in the input file, the program will print an error message to the output file. 

If there is a space in the middle of the prefix expression, the program will print an error message to
the output file.

The program is capable of handling many lines of input, the input file "many_lines_input.txt"
has 200000 lines of input. The program will take a few seconds to run through all the
lines of input. It is capable of doing so, warning though, the output will be very long.
(~30 mb output for 200000 lines of input)

Examples:
* -+ABC
* -A+BC
* $+-ABC+D-EF
* -\*A$B+C-DE*EF
* -+<101><12122><10023>
* -\<AABCD>+\<CCDA>\<WHYDIDIDOTHIS>
<pre>
* -+abc
* -A+bc
*    -+ABC
*   -+ABC
* -+ABC
* -+ABC
* -+ABC
*    -+ABC
*   -+ABC    
* -+123
* -1+23
* $+-123+4-56
* -\*1$2+3-45*56
</pre>
> WARNING: If you use <> in your input file, the program will not be able to solve the postfix expression.
> It will still convert the prefix expression to postfix, but it will not solve it,
> regardless if you use digits or letters.
