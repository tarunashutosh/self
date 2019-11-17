# This function removes spaces from between the > and <

def remove_spaces(ele):
	for i in range(len(ele)):
		if len(ele[i])==0:
			continue

		if ele[i][0] == ' ':
			ele[i] = ele[i][1:]
	return ele	
