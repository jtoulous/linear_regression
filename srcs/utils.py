import os
import csv
import pandas as pd

def getData():
    dataframe = pd.read_csv('data/data.csv')
    dataset = []
    features = list(dataframe.columns)

    for i in range(len(dataframe)):
        new_data = {}
        for feature in features:
            new_data[feature] = dataframe[feature][i]
        dataset.append(new_data)
    return dataset


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