#This code is the driver for training and testing on bibliographical data
from read_data import read_data
from training import training
from testing import testing
from newgen_output import verify
from find_labels import find_labels

train_data = read_data('IEEE_train.txt')
train_data1 = read_data('new_train.txt')
test_data = read_data('IEEE_test.txt')
test_data1 = read_data('new_testa.txt')
test_data2 = read_data('new_testb.txt')

train_data = train_data+train_data1
test_data = test_data + test_data1 + test_data2

tag_dict = find_labels(train_data+test_data)# + test_data + train_data1)
model, training_accuracy, pca, scaler = training(train_data, 'RandomForest', 'y', 'n', tag_dict)
testing_accuracy = testing(test_data, model, pca, scaler, 'n', tag_dict)
newgen_accuracy = verify(model, pca, scaler, 'n')

print ('The training accuracy:', training_accuracy)
print ('The testing accuracy:', testing_accuracy)
#print ('Verification accuracy:', newgen_accuracy)
