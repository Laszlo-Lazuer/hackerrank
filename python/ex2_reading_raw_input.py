# file: reading_raw_input.py
# Author: A. Laszlo Lazuer
# date: 01/17/17
# Python Version: 2.7
# description: Python Exercise #2 from hackerrank.com

#Task: Read a line of input from stdin and save it to a variable, . Then print the contents of  to stdout.

#Input Format

# A single line containing sentence s.
#
# Constraints
#  1 <= |s| <= 500
#
# Output Format
#
# Print the contents of s to stdout
#
# Print the contents of  to stdout.

#####
## This question isn't very clear to comprehend.  What it is asking for
## is that you request for an input, the program supplies the string, Then
## you must check the string length and only display it if it meets the
## conditions of the length to be greater than 1 and less or equal to 500.
#####

s = raw_input('') #Request input and store in s
length_check = len(s) #Store the value of the string length s into length_check
if ((length_check >= 1) & (length_check <= 500)):
        print s #If conditions are met print string s

#Verified passes all test cases
