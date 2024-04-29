import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import mean, stdev

from utils import getThetas, normalizeDataset, normalize, denormalize

def getData():
    dataFrame = pd.read_csv('data/data.csv')
    normData = {'means': {}, 'stds': {}}
    thetas = []
    km_list = []
    price_list = []
    features = list(dataFrame.columns)

    with open('data/thetas.txt', 'r') as file:
        for line in file:
            for value in line.split(','):
                thetas.append(float(value))

    for feature in features:
        normData['means'][feature] = mean(dataFrame[feature])
        normData['stds'][feature] = stdev(dataFrame[feature])

    for feature in dataFrame:
        for i in range(len(dataFrame)):
            value = normalize(dataFrame[feature][i], normData['means'][feature], normData['stds'][feature])
            if feature == 'km':
                km_list.append(value)
            elif feature == 'price':
                price_list.append(value)

    return km_list, price_list, thetas, normData
    


def getPredictionLine(x_limMin, x_limMax, thetas):
    x_prediction = []
    y_prediction = []

    for x in range(x_limMin, x_limMax):
        x_prediction.append(x)
        y_prediction.append(thetas[0] + (x * thetas[1]))

    return x_prediction, y_prediction


if __name__ == "__main__":
    try:
        x_limMin = -3
        x_limMax = 3
        y_limMin = -3
        y_limMax = 3

        x_km, y_price, thetas, normData = getData()
        x_prediction, y_prediction = getPredictionLine(-10, 10, thetas) 

        fig, ax = plt.subplots()

        ax.plot(x_km, y_price, 'o', color='blue', markersize=2)
        ax.plot(x_prediction, y_prediction, color='red')

        ax.set_title('Vehicules pricing')
        ax.set_xlabel('Mileage (km)')
        ax.set_ylabel('Price ($)')
        ax.set_xlim(x_limMin, x_limMax)
        ax.set_ylim(y_limMin, y_limMax)
        ax.set_xticks([])
        ax.set_yticks([])

        ax.set_facecolor('lightgray')
        ax.xaxis.set_major_formatter('{x:.1f}')
        ax.yaxis.set_major_formatter('{x:.1f}')

        plt.show()


    except Exception as error:
        print(error)