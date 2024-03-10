import csv
import os

def getDataset():
    dataset = []
    with open('utils/data.csv', 'r') as file:
        for line in file:
            if (line != "km,price\n"):
                dataset.append([float(x) for x in line.split(',')[:2]])
    return dataset
            
def saveThetas(theta0, theta1):
    os.remove('utils/thetas.txt')
    with open('utils/thetas.txt', 'w') as thetaFile:
        thetaFile.write(f"{theta0},{theta1}")

if __name__ == '__main__':
    try:
        learningRate = 0.00000000001
        dataset = getDataset()
        m = len(dataset)
        theta0 = 0
        theta1 = 0
        
        for epoch in range(30):
            print(f"==========  EPOCH {epoch}  ================")
            tmp_t0 = 0
            tmp_t1 = 0
            for data in dataset:
                mileage = data[0]
                price = data[1]
                estimatedPrice = round(theta0 + (theta1 * mileage), 5)
                print (f"for mileage of {mileage} with a value of {price}: prediction is {estimatedPrice}")
                tmp_t0 += (estimatedPrice - price)
                tmp_t1 += (estimatedPrice - price) * mileage
            tmp_t0 *= learningRate * (1/m)
            tmp_t1 *= learningRate * (1/m)

            theta0 = round(theta0 - tmp_t0, 10)
            theta1 = round(theta1 - tmp_t1, 10)
            print(theta0)
            print(theta1)
            print("===================================\n")
        saveThetas(theta0, theta1)

    except Exception as error:
        print(f"{error}")