# This function takes in features and their labels and write them to a file
import pandas as pd
from nltk.data import load
tagdict = load('help/tagsets/upenn_tagset.pickle')


def write_features_labels(out_dir, phrases, features, labels, case):
	columns = tagdict.keys() + ['num_words', 'num_numeric', 'phrase_position']
	df = pd.DataFrame(features, columns = columns)
	df.insert(loc=0, column='phrases', value=phrases)
	df1 = pd.DataFrame(labels, columns = ['label'])
	df['label'] = df1
	df.to_csv(out_dir + case +'.csv')
