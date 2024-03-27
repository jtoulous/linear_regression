import sys
import os
import subprocess

from utils.normalizer import normalizeDataset
from utils.utils import saveThetas

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "reset":
            saveThetas(0,0)
            os.remove("data/graph.png")
            exit()

        learningRate = 0.3
        norm, dataset = normalizeDataset()
        m = len(dataset)
        thetas = [0, 0]
        
        for epoch in range(300):
            print(f"==========  EPOCH {epoch}  ================")
            tmp_thetas = [0, 0]
            for data in dataset:
                mileage = data[0]
                price = data[1]
                estimatedPrice = thetas[0] + (thetas[1] * mileage)
                print (f"for mileage of {int(norm.denormalizeKm(mileage))} with a value of {int(norm.denormalizePrice(price))}: prediction is {int(norm.denormalizePrice(estimatedPrice))}")
            
                tmp_thetas[0] += (estimatedPrice - price)
                tmp_thetas[1] += (estimatedPrice - price) * mileage
                
            thetas[0] -=  (tmp_thetas[0] * (1/m) * learningRate)
            thetas[1] -=  (tmp_thetas[1] * (1/m) * learningRate)
            print("===================================\n")

        saveThetas(thetas[0], thetas[1])
        subprocess.run(["python", "graph.py"])

    except Exception as error:
        print(f"{error}")