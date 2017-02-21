# match comment strings
start_comment = '%'
end_comment = '\n'

# match keywords list
keywords = ['if', 'then', 'else', 'begin', 'end', 'while', 'do', 
			'program', 'var', 'as', 'int', 'bool']
# match symbols and operators list
symbols_and_operators = ['(', ')', ':=', ';', '*', 'div', 'mod', '+', '-', '=', '!=', 
						 '<', '>', '<=', '>=']

# match for built-in procedures
built_in = ['writeInt', 'readInt']

# match number, boollit, identifier regex's
number = r'[1-9][0-9]*|0' # range is 0..2147483647
boollit = r'false|true'
identifier = r'[a-z_A-Z][a-zA-Z0-9]*'

# dictionary of symbols and operators
symbols_and_operators_dict = {'(': 'LP', ')': 'RP', ':=': 'ASGN', ';': 'SC', '*': 'MULTIPLICATIVE(*)',
			'div': 'MULTIPLICATIVE(div)', 'mod': 'MULTIPLICATIVE(mod)', '+': 'ADDITIVE(+)',
			'-': 'ADDITIVE(-)', '=': 'COMPARE(=)', '!=': 'COMPARE(!=)', '<': 'COMPARE(<)',
			'>': 'COMPARE(>)', '<=': 'COMPARE(<=)', '>=': 'COMPARE(>=)'}

# list of keywords and symbols and operators and built-in procedures
tokens = keywords + symbols_and_operators + built_in
