from statistics import mean

from utils import getThetas
from normalizer import Normalizer, normalizeDataset

def calcMSE(normalizer, dataset, estimationList):
    totalError = 0
    for i in range(len(dataset)):
        realPrice = normalizer.denormalizePrice(dataset[i][1])
        totalError += (realPrice - estimationList[i]) ** 2
    
    return totalError / len(dataset)

def calcRsquared(normalizer, dataset, estimationList):
    realPriceList = []
    ss_tot = 0
    ss_res = 0

    for i in range(len(dataset)):
        realPriceList.append(normalizer.denormalizePrice(dataset[i][1]))
    
    for i in range(len(realPriceList)):
        ss_tot += (realPriceList[i] - mean(realPriceList)) ** 2

    for i in range(len(realPriceList)):
        ss_res += (realPriceList[i] - estimationList[i]) ** 2

    return 1 - (ss_res / ss_tot) 


if __name__ == "__main__":
    try:
        normalizer, dataset = normalizeDataset()
        thetas = getThetas()
        estimationList = []

        for data in dataset:
            estimatedPrice = thetas[0] + thetas[1] * data[0]
            estimationList.append(normalizer.denormalizePrice(estimatedPrice))
        
        mse = calcMSE(normalizer, dataset, estimationList)
        r_squared = calcRsquared(normalizer, dataset, estimationList)

        print (f"Mean Squared Error = {mse}")
        print (f"R-squared = {r_squared}")

    except Exception as error:
        print(error)