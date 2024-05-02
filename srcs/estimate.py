import pandas as pd

from utils import getThetas

if __name__ == "__main__":
    try:
        userInput = float(input("mileage: "))
        if userInput < 0:
            raise Exception("Error: mileage can't be negatif")

        thetas = getThetas()
        estimatedPrice = int(thetas[0] + (thetas[1] * userInput))

        if estimatedPrice < 0:
            print(f"the estimated price for your vehicule is 0$")
        else:
            print(f"the estimated price for your vehicule is {estimatedPrice}$")

    except Exception as error:
        print(error)