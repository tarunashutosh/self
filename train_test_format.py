# This function takes in train and test data in word tag format and combines them to get the required phrase tag format
from read_data import read_data
from get_phrase_tags import individual_phrase_tags
from find_labels import find_labels
import sys
def arrange(files):
	new_data_tags = read_data(files)
	phrase_file= files.split('.')[:-2][0]+'.words.txt'
	new_data_phrases = read_data(phrase_file)
	f = open('new_'+files.split('/')[-1].split('.')[0]+'.txt', 'w')
	for i,line in enumerate(new_data_tags):
		tags = line.split()
		if len(tags)==0:
			continue
		words = new_data_phrases[i].split()
		temp = '<' + tags[0] + '>' + words[0]
		prev_tag = tags[0]
		for j,ele in enumerate(tags[1:]):
			if ele==prev_tag:
				temp = temp + ' ' + words[j+1]
			else:
				temp = temp + ', </' + prev_tag + '>' + '<' + ele + '>' + words[j+1]
				prev_tag = ele
		temp = temp+'</' + prev_tag + '>\n'
		f.write(temp)
	f.close()
filenames=[sys.argv[1]]#['/home/ashutosh/self/training_data_1nov2019/train.tags.txt']	
for ele in filenames:
	arrange(ele)

'''data = read_data('new_data.txt')
#data = read_data('IEEE_train.txt')
tag_dict = find_labels(data)
ind_tags_phrases = individual_phrase_tags(data, tag_dict)
print ind_tags_phrases'''
