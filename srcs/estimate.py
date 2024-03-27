from colorama import Fore, Style
from utils.normalizer import Normalizer, normalizeDataset
from utils.utils import getThetas
from utils.logs import printLog, printInfo, printError

def getInput():
    try:
        userInput = float(input(f"{Fore.LIGHTBLUE_EX}\nmileage: "))
        print(f"{Style.RESET_ALL}")
        if userInput < 0:
            raise Exception("error: mileage can't be negative")

    except ValueError:
        raise Exception("error: argument can't be converted to float")
    except Exception as error:
        raise Exception(error)
        
    return userInput        

if __name__ == "__main__":
    try:
        userInput = getInput()
        normalizer, dataset = normalizeDataset(userInput=userInput)
        thetas = getThetas()

        estimatedPrice = thetas[0] + (thetas[1] * normalizer.normalizeKm(userInput))
        printLog(f"=========> the estimated price for your vehicule is {int(normalizer.denormalizePrice(estimatedPrice))}$\n")

    except Exception as error:
        printError(f"{error}")