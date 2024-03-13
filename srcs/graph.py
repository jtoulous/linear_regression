import matplotlib.pyplot as plt
import numpy as np

from normalizer import Normalizer, normalizeDataset
from utils import getThetas

def getData():
    dataset = []
    km_list = []
    price_list = []

    normalizer, dataset = normalizeDataset()
    for data in dataset:
        km_list.append(float(data[0]))
        price_list.append(float(data[1]))

    return np.array(km_list), np.array(price_list)


def getPredictionLine(x_limMin, x_limMax):
    thetas = getThetas()
    x_prediction = []
    y_prediction = []

    for x in range(x_limMin, x_limMax):
        x_prediction.append(x)
        y_prediction.append(thetas[0] + (x * thetas[1]))

    return x_prediction, y_prediction


if __name__ == "__main__":
    try:
        x_limMin = -0.5
        x_limMax = 1.5
        y_limMin = -0.5
        y_limMax = 1.5

        x_km, y_price = getData()
        x_prediction, y_prediction = getPredictionLine(-5, 5) 

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