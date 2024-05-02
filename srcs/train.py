import sys
import subprocess
import pandas as pd

from utils import saveThetas, getData

def checkArgs():
        if len(sys.argv) > 1 and sys.argv[1] == "reset":
            saveThetas(0, 0)
            exit()
        
        elif len(sys.argv) > 1:
            raise Exception("Error: no arguments needed")


if __name__ == '__main__':
    try:
        checkArgs()

        dataset = getData()
        m = len(dataset)
        learningRateT0 = 0.1
        learningRateT1 = 0.0000000001
        thetas = [0, 0]
        
        for epoch in range(300):
            print(f"==========  EPOCH {epoch}  ================")
            tmp_thetas = [0, 0]
            for data in dataset:
                estimatedPrice = thetas[0] + (thetas[1] * data['km'])
                print (f"for mileage of {data['km']} with a value of {data['price']}: prediction is {estimatedPrice}")            
                tmp_thetas[0] += (estimatedPrice - data['price'])
                tmp_thetas[1] += (estimatedPrice - data['price']) * data['km']
                
            thetas[0] -=  ((tmp_thetas[0] / m) * learningRateT0)
            thetas[1] -=  ((tmp_thetas[1] / m) * learningRateT1)
            print("===================================\n")

        saveThetas(thetas[0], thetas[1])
        subprocess.run(["python", "graph.py"])

    except Exception as error:
        print(error)