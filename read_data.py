# This function takes in the path to a file as input and reads the contents
def read_data(inp_file):
	data = []
	f = open(inp_file, 'r')
	for row in f:
		data.append(row)
	return data
