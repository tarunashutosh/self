# This function takes in individual phrases and their tags and crafts features for them
import sys
import numbers
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
from nltk.data import load
tagdict = load('help/tagsets/upenn_tagset.pickle')
stop_words = set(stopwords.words('english'))

def pos_tags(phrase, position):
	words =  nltk.word_tokenize(phrase)	
	tagged = nltk.pos_tag(words)
	pos_count = [0]*len(tagdict.keys())
	pos_order = '' 
	for ele in tagged:
		pos_count[tagdict.keys().index(ele[1])] += 1
		pos_order += ' ' + ele[1]
	nums = 0
	for x in words:
		try:
			x = float(x)
			nums+=1
		except:
			continue
	feat = pos_count + [str(len(words))] + [str(nums)] + [str(position)]#+[len(phrase)]#+[str(position)]
	return feat

def extract_features(all_phrases, phrase_position, step):
	features = []
	for i,ele in enumerate(all_phrases):
#		print ('Extracting features for {}'.format(step))
		features.append(pos_tags(ele, phrase_position[i]))
	return features
