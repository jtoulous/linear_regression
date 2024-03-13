from normalizer import Normalizer, normalizeDataset
from utils import getThetas

if __name__ == "__main__":
    try:
        userInput = float(input("mileage: "))
        #checkInput(userInput)

        normalizer, dataset = normalizeDataset(userInput=userInput)
        thetas = getThetas()

        estimatedPrice = thetas[0] + (thetas[1] * normalizer.normalizeKm(userInput))
        print(f"the estimated price for your vehicule is {normalizer.denormalizePrice(estimatedPrice)}")

    except Exception as error:
        print(f"{error}")