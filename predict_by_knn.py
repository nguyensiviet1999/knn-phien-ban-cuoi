from math import sqrt
import pickle
import pandas as pd
import re
import time

X_data_tf = pickle.load(open('X_data_tf.pkl', 'rb'))
y_data = pickle.load(open('y_data.pkl', 'rb'))

X_test_tf = pickle.load(open('X_test_tf.pkl', 'rb'))
y_test = pickle.load(open('y_test.pkl', 'rb'))

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for word in row1:
		if word in row2:
			distance += (row1[word] - row2[word])**2
		else:
			distance += row1[word]**2
	for word in row2:
		if word in row1:
			pass
		else:
			distance += row2[word]**2
	return sqrt(distance)
# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for i in range(len(train)):
		dist = euclidean_distance(test_row, train[i])
		distances.append((i, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i])
	return neighbors

# Make a classification prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	resultTemp = list()
	resultTemp_key=[]
	for row,dist in neighbors:
		if dist == 0.0:
			resultTemp = list()
			resultTemp_key=[]
			resultTemp.append((y_data[row],int(99999)))
			resultTemp_key.append(y_data[row])
			break
		else:
			resultTemp.append((y_data[row],1/dist))
			resultTemp_key.append(y_data[row])
	output_values = dict.fromkeys(set(resultTemp_key).union(), 0)
	for label,weight in resultTemp:
		output_values[label] += weight
	prediction = max(set(output_values), key=lambda k: output_values[k])
	return prediction

def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0
def predict_test():
	predict_test = []
	for row in range(len(X_test_tf)):
		predict_test.append(predict_classification(X_data_tf,X_test_tf[row],3))
	print(accuracy_metric(y_test,predict_test))