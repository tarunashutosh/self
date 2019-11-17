# This function takes in original text, separated by commas and breaks them into individual phrase and tag
import re
from remove_spaces import remove_spaces
import sys
def individual_phrase_tags(data):
	ind_phrases = []
	for row in data:
		phrases = row.split(',')
		for i,ele in enumerate(phrases):
			ind_phrases.append([ele,i])
	ind_tags_phrases = []
	regex = re.compile('[^0-9a-zA-Z,%\' - )(]')
	for k,ele in enumerate(ind_phrases):
		while (ele[0]):
			if '>' not in ele[0]:
				break
			a = ele[0].split('>')
			a = remove_spaces(a)
			new_tag, flag  = '', 0
			for i,ele1 in enumerate(a):
				if ele1.startswith('<'):
					new_tag = new_tag + ele1[1:] + ' '
				else:
					try:
						ind = ele1.index('<')
					except:
						new_tag = new_tag + ',' + ele1
						flag = 1
						new_tag = regex.sub('', new_tag)
						if new_tag.split(',')[0]!='' and new_tag.split(',')[1]!='':
							new_tag = new_tag.split(',')[0].split(' ')[-2] + ',' + new_tag.split(',')[1]
							ind_tags_phrases.append([new_tag,ele[1]])
						break
					new_tag = new_tag + ',' + ele1[:ind]
					new_tag = regex.sub('', new_tag)
					if new_tag.split(',')[0]!='' and new_tag.split(',')[1]!='':
						new_tag = new_tag.split(',')[0].split(' ')[-2] + ',' + new_tag.split(',')[1]
						ind_tags_phrases.append([new_tag,ele[1]])
					ele = ele1[ind:] + '>' + '>'.join(a[i+1:])
					break
			if flag==1:
				break
	return ind_tags_phrases
