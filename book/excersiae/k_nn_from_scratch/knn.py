import numpy as np
from math import sqrt
from csv import reader
from random import randrange

def euclidean_distance(x, y):
    distance = 0.0
    for i in range(len(x) - 1):
        distance += (x[i] - y[i])**2
    return sqrt(distance)

def get_neighbors(train_data, test_row, num_neighbors):
    distances = []
    for index, row in enumerate(train_data):
        d = euclidean_distance(test_row, row)
        distances.append((index, d))
    
    n = len(distances)

    for i in range(n):
        min = i
        for j in range(i, n):
            if distances[j][1] < distances[min][1]:
                min = j
        if min != i:
            tmp = distances[i]
            distances[i] = distances[min]
            distances[min] = tmp

    neighbors = []
    for i in range(num_neighbors):
        neighbors.append(train_data[distances[i][0]])
    return neighbors

def load_csv(filename):
	dataset = []
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def str_column_to_int(dataset, column):
    class_values = [row [column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

def cross_validation_split(dataset, n_folds):
    dataset_split = []
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for _ in range(n_folds):
        fold = []
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split

def accuracy_metric(actual, predicted):
    correct = 0
    size = len(actual)
    for i in range(size):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(size) * 100

def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction
# kNN Algorithm
def k_nearest_neighbors(train, test, num_neighbors):
    predictions = []
    for row in test:
        output = predict_classification(train, row, num_neighbors)
        predictions.append(output)
    return predictions

def evaluate_algorithm(dataset, algorith, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = []
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list(fold)

        predicted = algorith(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores

dataset = load_csv('./iris.csv')
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)

# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)

n_folds = 5
num_neighbors = 5

scores = evaluate_algorithm(dataset, k_nearest_neighbors, n_folds, num_neighbors)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))