from lexer_constants import *
from lexer_automaton import automaton
from lexer_functions import *
from re import fullmatch
# instantiate automaton
lexer = automaton('entry')
# name of source file
#f_in = 'test.tl'
#f_in = '../Examples/Simple/simple1.tl'
#f_in = '../Examples/sqrt/sqrt.tl'
f_in = '../Examples/type-error1.tl'
# name of output file
#f_out = 'test.tok'
#f_out = 'simpl1.tok'
#f_out = 'sqrt.tok'
f_out = 'type-error1.tok'
f_out = open(f_out, 'w')
# read lines of input file
with open(f_in) as f:
	lines = f.readlines()

	# iterate over each line
	for line in lines:
		line = line.strip()
		# lexical tokens are separated by spaces
		tokens = line.split(' ')
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
				stop()



	f.close()

f_out.close()



