#This code is the driver for training and testing on bibliographical data
from read_data import read_data
from training import training
from testing import testing
from newgen_output import verify
train_data = read_data('/home/ashutosh/research/newgen/references/orig/IEEE_train.txt')
test_data = read_data('/home/ashutosh/research/newgen/references/orig/IEEE_test.txt')
model, training_accuracy, pca, scaler = training(train_data, 'RandomForest', 'y', 'n')
testing_accuracy = testing(test_data, model, pca, scaler, 'n')
newgen_accuracy = verify(model, pca, scaler, 'n')
print ('The training accuracy:', training_accuracy)
print ('The testing accuracy:', testing_accuracy)
print ('Verification accuracy:', newgen_accuracy)
