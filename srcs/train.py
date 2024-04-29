import sys
import subprocess
import pandas as pd

from utils import saveThetas, normalizeDataset, normalize, denormalize
from statistics import mean, stdev

def normalize(value, mean, std):
    return (value - mean) / std

def denormalize(value, mean, std):
    return (value * std) + mean

def normalizeDataset():
    normData = {'means': {}, 'stds': {}}
    dataframe = pd.read_csv('data/data.csv')
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


def checkArgs():
        if len(sys.argv) > 1 and sys.argv[1] == "reset":
            saveThetas(0, 0)
            exit()
        
        elif len(sys.argv) > 1:
            raise Exception("Error: no arguments needed")


if __name__ == '__main__':
    try:
        checkArgs()

        learningRate = 0.3
        dataset, normData = normalizeDataset()
        m = len(dataset)
        thetas = [0, 0]
        
        for epoch in range(300):
            print(f"==========  EPOCH {epoch}  ================")
            tmp_thetas = [0, 0]
            for data in dataset:
                km = data['km']
                price = data['price']
                estimatedPrice = thetas[0] + (thetas[1] * km)
                print (f"for mileage of {int(denormalize(km, normData['means']['km'], normData['stds']['km']))} " 
                    f"with a value of {int(denormalize(price, normData['means']['price'], normData['stds']['price']))}: "
                    f"prediction is {int(denormalize(estimatedPrice, normData['means']['price'], normData['stds']['price']))}")
            
                tmp_thetas[0] += (estimatedPrice - price)
                tmp_thetas[1] += (estimatedPrice - price) * km
                
            thetas[0] -=  (tmp_thetas[0] * (1/m) * learningRate)
            thetas[1] -=  (tmp_thetas[1] * (1/m) * learningRate)
            print("===================================\n")

        saveThetas(thetas[0], thetas[1])
        subprocess.run(["python", "graph.py"])

    except Exception as error:
        print(error)