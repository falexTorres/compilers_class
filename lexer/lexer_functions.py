def output_error(msg, f_out):
	f_out.write(msg + '\n')

def output_success(msg, f_out):
	f_out.write(msg + '\n')

def get_tokens(line):
	tokens = []
	build_token = ''
	for l in line:
		if build_token in tokens:
			tokens.append(build_token)
			build_token = ''
		elif l in tokens and build_token == '':
			tokens.append(l)
		elif l in tokens:
			tokens.append(build_token)
			tokens.append(l)
			build_token = ''
		elif l == ' ' and build_token != '':
			tokens.append(build_token)
			build_token = ''
		elif l == ' ' and build_token == '':
			continue
		else:
			build_token += l
	if build_token != '':
		tokens.append(build_token)

	return tokens