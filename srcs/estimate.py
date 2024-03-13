from normalizer import Normalizer, normalizeDataset
from utils import getThetas

if __name__ == "__main__":
    try:
        userInput = float(input("mileage: "))
        #checkInput(userInput)

        normalizer, dataset = normalizeDataset(userInput=userInput)
        thetas = getThetas()

        estimatedPrice = thetas[0] + (thetas[1] * normalizer.normalizeKm(userInput))
        
        if thetas[0] == 0 and thetas[1] == 0:
            print(f"the estimated price for your vehicule is 0$")
        else:
            print(f"the estimated price for your vehicule is {int(normalizer.denormalizePrice(estimatedPrice))}$")

    except Exception as error:
        print(f"{error}")