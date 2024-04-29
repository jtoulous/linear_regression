import pandas as pd

from statistics import mean, stdev
from utils import getThetas, normalizeDataset, normalize, denormalize

if __name__ == "__main__":
    try:
        normData = {'means': {}, 'stds': {}}
        dataframe = pd.read_csv('data/data.csv')
        features = list(dataframe.columns)
        
        userInput = float(input("mileage: "))
        if userInput < 0:
            raise Exception("Error: mileage can't be negatif")

        for feature in features:
            normData['means'][feature] = mean(dataframe[feature])
            normData['stds'][feature] = stdev(dataframe[feature])

        thetas = getThetas()

        estimatedPrice = thetas[0] + (thetas[1] * normalize(userInput, normData['means']['km'], normData['stds']['km']))
        estimatedPrice = int(denormalize(estimatedPrice, normData['means']['price'], normData['stds']['price']))
        if estimatedPrice < 0:
            print(f"the estimated price for your vehicule is 0$")
        else:
            print(f"the estimated price for your vehicule is {estimatedPrice}$")

    except Exception as error:
        print(f"{error}")