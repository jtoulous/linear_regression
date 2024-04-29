import os
import csv

def normalize(value, mean, std):
    return (value - mean) / std

def denormalize(value, mean, std):
    return (value * std) + mean

def normalizeDataset():
    dataframe = pd.read_csv('data/data.csv')
    normData = {'means': {}, 'stds': {}}
    dataset = []
    features = list(dataframe.columns)

    for feature in features:
        normData['means'][feature] = mean(dataframe[feature])
        normData['stds'][feature] = stdev(dataframe[feature])

    for i in range(len(dataframe)):
        new_data = {}
        for feature in features:
            new_data[feature] = normalize(dataframe[feature][i], normData['means'][feature], normData['stds'][feature])
        dataset.append(new_data)
    return dataset, normData


def saveThetas(theta0, theta1):
    if os.path.exists('data/thetas.txt'):    
        os.remove('data/thetas.txt')
    with open('data/thetas.txt', 'w') as thetaFile:
        thetaFile.write(f"{theta0},{theta1}")
    

def getThetas():
    with open('data/thetas.txt', 'r') as thetaFile:
        content = thetaFile.read()
        thetas = [float(x) for x in content.split(',')[:2]]
    return thetas