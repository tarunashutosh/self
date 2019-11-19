# This function finds the existing labels and corrects unidentifiable instances of them
import re
import numpy as np
import sys
import json
import os

def find_labels(data):
	if not os.path.exists('tag_names.json'):
		tags = []
		regex = re.compile('[^0-9a-zA-Z]')
		tag_dict = {}
		for citation in data:
			positions = [x.start() for x in re.finditer('<', citation)]
			for ele in positions:
				j= ele+1
				temp_tag = ''
				while not citation[j].isalnum():
					if citation[j]=='/':
						k = j+1
						while citation[k]!='>':
							temp_tag+= citation[k]
							k+= 1
						tags.append(regex.sub('',temp_tag))
						break
					j+=1
		tags = np.unique(tags)
		print (tags)
		new_tags = []
		for ele in tags:
			choice = raw_input('Is the tag name:\'{}\' acceptable? (y/n): '.format(ele))
			if choice.lower()[0]!='y':
				temp = raw_input('Please enter a suitable tag name instead, for \'{}\': '.format(ele))
				tag_dict[ele] = temp
				new_tags.append(temp)
			else:
				tag_dict[ele] = ele
				new_tags.append(ele)
		with open('./tag_names.json','w') as f:
			f.write(json.dumps(tag_dict))
	else:
		with open('./tag_names.json', 'r') as f:
			tag_dict = json.load(f)
	return tag_dict
