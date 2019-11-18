# This code reads in the existing predictions and compares it with a separate model
import pandas as pd
from extract_features import extract_features
from sklearn import metrics

def verify(model, pca, scaler, apply_pca):
#def verify():
	file_path = 'Output_of_NUS_Parse/'
	file_name = 'Ref_classification_samples2Nov.xlsx'
	df = pd.read_excel(file_path+file_name, sheet_name='predicted_ref_class_samples')
	#print (df['predicted'])
	pred_tags_overall, ind_tags_overall = [], []
	results=[]
	for ele in df['predicted']:
		ind_phrases, ind_tags, phrase_position = [], [], []
		elements=[i for i in ele.split('\n') if len(i)!=0]
		#print (elements)
#		break

		for j,i in enumerate(elements):
			ind_phrases.append(':'.join(i.split(':')[1:]))
			ind_tags.append(i.split(':')[0])
			phrase_position.append(j)
		#	print (':'.join(i.split(':')[1:]), i.split(':')[0], j)
#	print (ind_phrases[:5], ind_tags[:5], phrase_position[:5])
		test_features = extract_features(ind_phrases, phrase_position, 'testing')
		if apply_pca == 'y':
			test_features = scaler.transform(test_features)
			test_features = pca.transform(test_features)
		pred_tags = model.predict(test_features)
		pred_tags_overall.append(pred_tags)
		ind_tags_overall.append(ind_tags)
		temp=''
		for j,i in enumerate(pred_tags):
			temp = temp + i+':'+ind_phrases[j]+'\n'
		results.append(temp)
	df['verified']=results
	df.to_excel('Output_of_NUS_Parse/verified_'+file_name, sheet_name='verified')
	#accuracy = metrics.accuracy_score(ind_tags_overall, pred_tags_overall)
	#return accuracy
#verify()
