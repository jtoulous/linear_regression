import matplotlib.pyplot as plt
import numpy as np
import csv

def getData():
    dataset = []
    km_list = []
    price_list = []

    with open('utils/data.csv', 'r') as csvFile:
        csvContent = csv.reader(csvFile, delimiter=',')
        for row in csvContent:
            dataset.append(row)
        dataset.pop(0)
   
    for data in dataset:
        km_list.append(float(data[0]))
        price_list.append(float(data[1]))
    return np.array(km_list), np.array(price_list)


def getPredictionLine(x_lim):
    theta0, theta1 = getThetas()
    x_prediction = []
    y_prediction = []

    for x in range(x_lim):
        x_prediction.append(x)
        y_prediction.append(theta0 + (x * theta1))
    return x_prediction, y_prediction


def getThetas():
    with open('utils/thetas.txt', 'r') as thetaFile:
        content = thetaFile.read()
        thetas = [float(x) for x in content.split(',')[:2]]
    return thetas[0], thetas[1]


if __name__ == "__main__":
    try:
        x_lim = 250000
        y_lim = 9000

        x_km, y_price = getData()
        x_prediction, y_prediction = getPredictionLine(x_lim) 

        fig, ax = plt.subplots()

        ax.plot(x_km, y_price, 'o', color='blue', markersize=2)
        ax.plot(x_prediction, y_prediction, color='red')

        ax.set_title('Vehicules pricing')
        ax.set_xlabel('Mileage (km)')
        ax.set_ylabel('Price ($)')
        ax.set_xlim(0, x_lim)
        ax.set_ylim(0, y_lim)

        ax.set_facecolor('lightgray')
        ax.xaxis.set_major_formatter('{x:.0f}')
        ax.yaxis.set_major_formatter('{x:.0f}')

        plt.show()


    except Exception as error:
        print(error)