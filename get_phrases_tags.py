# This function takes in original text, separated by commas and breaks them into individual phrase and tag
import re
from remove_spaces import remove_spaces
import sys
from find_labels import find_labels

def individual_phrase_tags(data):

	tag_dict = find_labels(data)
	ind_tags_phrases = []
	for citation in data:
		positions = [x.start() for x in re.finditer('<', citation)]
		temp_positions = []
		regex = re.compile('[^0-9a-zA-Z]')
		for i,ele in enumerate(positions[:-1]):
			temp_tag1, temp_tag2= '', ''
			j1, j2 = positions[i]+1, positions[i+1]+1
			while citation[j1]!='>':
				temp_tag1+= citation[j1]
				j1+= 1
			while citation[j2]!='>':
				temp_tag2+= citation[j2]
				j2+= 1
			if regex.sub('', temp_tag1).lower() == regex.sub('', temp_tag2).lower():
				temp_positions.append(positions[i+1])
		positions = temp_positions

		for i,ele in enumerate(positions):
			temp_tag, temp_phrase = '', '' 
			j=ele+1
			while citation[j]!='>':
				if citation[j].isalnum():
					temp_tag+= citation[j]
				j+= 1
			temp_tag = regex.sub('', temp_tag)
			temp_tag = tag_dict[temp_tag]
			
			regex = re.compile('[^0-9a-zA-Z,%\' - )(]')				
			j=ele-1
			while citation[j]!='>':
				temp_phrase+= citation[j]
				j-=1
			temp_phrase = ''.join(reversed(regex.sub('', temp_phrase)))
			ind_tags_phrases.append([temp_tag+','+temp_phrase, i])

	return ind_tags_phrases
