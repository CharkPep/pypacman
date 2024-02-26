import json

FILE = "levels/originalPoints.txt"


def convertTxtToJson(file):
    with open(file, "r") as f:
        lines = f.readlines()
        lines = [list(line[:len(line) - 1]) for line in lines]
        return lines


for line in convertTxtToJson(FILE):
    print(json.dumps(line) + ", ")
