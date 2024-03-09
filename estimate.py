def getThetas():
    with open("thetas.txt", "r") as file:
        content = file.read()
        thetas = [float(x) for x in content.split(',')[:2]]
        return thetas

if __name__ == "__main__":
    try:
        thetas = getThetas()
        mileage = float(input("mileage: "))
        print(f"the estimated price for your vehicule is {thetas[0] + (thetas[1] * mileage)}")

    except Exception as error:
        print(f"{error}")