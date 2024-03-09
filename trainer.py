import csv

def getDataset():
    dataset = []
    with open('data.csv', 'r') as file:
        for line in file:
            if (line != "km,price\n"):
                dataset.append([float(x) for x in line.split(',')[:2]])
    return dataset
            

if __name__ == '__main__':
    try:
        learningRate = 0.01
        dataset = getDataset()
        m = len(dataset)
        theta0 = 0
        theta1 = 0
        
        for epoch in range(100):
            print(f"==========  EPOCH {epoch}  ================")
            tmp_t0 = 0
            tmp_t1 = 0
            for data in dataset:
                mileage = data[0]
                price = data[1]
                estimatedPrice = round(theta0 + (theta1 * mileage), 5)
                print (f"for mileage of {mileage} with a value of {price}: {estimatedPrice}")
                tmp_t0 += (estimatedPrice - price)
                tmp_t1 += (estimatedPrice - price) * mileage
            tmp_t0 *= learningRate * (1/m)
            tmp_t1 *= learningRate * (1/m)

            theta0 -= tmp_t0
            theta1 -= tmp_t1
            print(theta0)
            print(theta1)
            print("===================================\n")

    except Exception as error:
        print(f"{error}")