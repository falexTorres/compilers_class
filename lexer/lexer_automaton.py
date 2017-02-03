from lexer_constants import *
from re import fullmatch

class automaton:
	def __init__(this, state):
		this.state = state

	def __getTokenType(this, token):
		if token == '%':
			return 'comment'
		elif this.__isBuiltIn(token):
			return 'built in procedures'
		elif this.__isKeyword(token):
			return 'keywords'
		elif this.__isSymbolOrOperator(token):
			return 'symbols and operators'
		elif this.__isNumOrBoollitOrIdentifier(token):
			return 'num, boollit, identifier'

	def __isBuiltIn(this, token):
		if token in built_in:
			return True

	def __isKeyword(this, token):
		if token in keywords:
			return True

	def __isNum(this, token):
		match = fullmatch(number, token)
		if match:
			return True

	def __isBoollit(this, token):
		match = fullmatch(boollit, token)
		if match:
			return True

	def __isIdentifier(this, token):
		match = fullmatch(identifier, token)
		if match:
			return True

	def __isSymbol(this, token):
		if token in symbols:
			return True

	def __isOperator(this, token):
		if token in operators:
			return True

	def __isNumOrBoollitOrIdentifier(this, token):
		return this.__isNum(token) or this.__isBoollit(token) or this.__isIdentifier(token)

	def __isSymbolOrOperator(this, token):
		return this.__isSymbol(token) or this.__isOperator(token)

	# only non-private function
	def process_token(this, token):
		if this.state == 'entry':
			this.state = this.__getTokenType(token)

		# switch statement for automaton state
		if this.state == 'comment':
			if token == '\n':
				this.state = 'entry'
			return ('', 'token ignored')

		elif this.state == 'num, boollit, identifier':
			if this.__isNum(token):
				this.state = 'entry'
				return ('success', 'num(' + str(token) + ')')
			elif this.__isBoollit(token):
				this.state = 'entry'
				return ('success', 'boollit(' + str(token) + ')')
			elif this.__isIdentifier(token):
				this.state = 'entry'
				return ('success', 'ident(' + str(token) + ')')

		elif this.state == 'built in procedures':
			this.state = 'entry'
			return ('success', token.upper())

		elif this.state == 'symbols and operators':
			this.state = 'entry'
			return ('success', symbols_and_operators_dict[token])

		elif this.state == 'keywords':
			this.state = 'entry'
			return ('success', token.upper())

		else:
			this.state = 'entry'
			return ('error', 'lexical error')