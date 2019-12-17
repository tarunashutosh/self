# This function takes in the training data and trains models using different algorithms
import sys
import numpy as np
from get_phrase_tags import individual_phrase_tags
from extract_features import extract_features
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn import svm, naive_bayes, neural_network, linear_model, discriminant_analysis
from sklearn import metrics
from sklearn.multiclass import OneVsRestClassifier
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from  write_features_labels import write_features_labels

def training(data, classifier, one_vs_all, apply_pca, tag_dict):
	ind_tags_phrases = individual_phrase_tags(data, tag_dict)
	ind_phrases, ind_tags, phrase_position = [], [], []


	for i in ind_tags_phrases:
		ind_phrases.append(i[0].split(',')[1])
		ind_tags.append(i[0].split(',')[0])
		phrase_position.append(i[1])
	print ('train', len(ind_phrases))

	train_features = extract_features(ind_phrases, phrase_position, 'training')
	write_features_labels('./', ind_phrases, train_features, ind_tags, 'train_features')
	pca, scaler = '', ''
	if apply_pca == 'y':
		scaler = StandardScaler()
		scaler.fit(train_features)
		train_features = scaler.transform(train_features)
		pca = PCA(0.95)
		pca.fit(train_features)
		train_features = pca.transform(train_features)
	model = OneVsRestClassifier(RandomForestClassifier(n_estimators=100), n_jobs = -1)
	model.fit(train_features, ind_tags)
	pred_tags = model.predict(train_features)
	accuracy = metrics.accuracy_score(ind_tags, pred_tags)
	return model, accuracy, pca, scaler
