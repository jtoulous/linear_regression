import csv
import os

class Normalizer:
    def __init__(self, kmData, priceData, userInput=None):
        if userInput is None:    
            self.maxKm = max(kmData)
            self.minKm = min(kmData)
        else:
            self.maxKm = max(*kmData, userInput)
            self.minKm = min(*kmData, userInput)
        self.maxPrice = max(priceData)
        self.minPrice = min(priceData)
 
    def normalizeKm(self, value):
        return (value - self.minKm) / (self.maxKm - self.minKm)

    def denormalizeKm(self, value):
        return value * (self.maxKm - self.minKm) + self.minKm

    def normalizePrice(self, value):
        return (value - self.minPrice) / (self.maxPrice - self.minPrice)

    def denormalizePrice(self, value):
        return value * (self.maxPrice - self.minPrice) + self.minPrice


def normalizeDataset(userInput=None):
    dataset = []
    kmData = []
    priceData = []

    with open('data/data.csv', 'r') as file:
        for line in file:
            if (line != "km,price\n"):
                kmData.append(float(line.split(',')[0]))
                priceData.append(float(line.split(',')[1]))
    
    normalizer = Normalizer(kmData, priceData, userInput=userInput)
    for i in range(len(kmData)):
        dataset.append([normalizer.normalizeKm(kmData[i]), normalizer.normalizePrice(priceData[i])])

    #with open('normalized_data.csv', 'w', newline='') as csvFile:
    #    writer = csv.writer(csvFile)
    #    writer.writerow(['km', 'price'])
    #    for data in dataset:
    #        writer.writerow(data)

    return normalizer, dataset