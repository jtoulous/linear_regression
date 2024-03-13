import sys
import subprocess

from normalizer import Normalizer, normalizeDataset
from utils import saveThetas

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "reset":
            saveThetas(0,0)
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
            
            tmp_thetas[0] *= learningRate * (1/m)
            tmp_thetas[1] *= learningRate * (1/m)
            thetas[0] -=  tmp_thetas[0]
            thetas[1] -=  tmp_thetas[1]
            print("===================================\n")

        #print (f"t0: {thetas[0]})
        #print (f"t1: {thetas[1]})
        saveThetas(thetas[0], thetas[1])
        subprocess.run(["python", "graph.py"])

    except Exception as error:
        print(f"{error}")