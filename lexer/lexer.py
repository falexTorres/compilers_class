import sys
import os
from lexer_constants import *
from lexer_automaton import automaton
from lexer_functions import *
from re import fullmatch
# instantiate automaton
lexer = automaton('entry')
# read command line arguments for file
if len(sys.argv) <= 1:
	print("\nplease provide the source file path as a command argument\n")
	sys.exit()
f_in = sys.argv[1]
if f_in[-2:] != 'tl':
	print("\nthe source file must have a '.tl' extension\n")
	sys.exit()
elif not os.path.isfile(f_in):
	print("\nsource file cannot be found\n")
	sys.exit()
# name of output file
f_out = f_in[:-2] + 'tok'
f_out = './' + f_out.split('/')[-1]
f_out = open(f_out, 'w')
# read lines of input file
with open(f_in) as f:
	lines = f.readlines()
	# iterate over each line
	for line in lines:
		line = line.strip()
		# lexical tokens are separated by spaces
		tokens = get_tokens(line)
		# iterate over tokens in line
		for token in tokens:
			if token == '':
				continue
			(status, msg) = lexer.process_token(token)
			if status == 'error':
				output_error(msg, f_out)
			elif status == 'success':
				output_success(msg, f_out)
			else:
				if msg == 'token ignored':
					continue
				print("error returning from function process_token")
				sys.exit()
	f.close()
f_out.close()



