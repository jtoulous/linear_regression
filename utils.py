import os
import csv

def saveThetas(theta0, theta1):
    os.remove('data/thetas.txt')
    with open('data/thetas.txt', 'w') as thetaFile:
        thetaFile.write(f"{theta0},{theta1}")

def getThetas():
    with open('data/thetas.txt', 'r') as thetaFile:
        content = thetaFile.read()
        thetas = [float(x) for x in content.split(',')[:2]]
    return thetas