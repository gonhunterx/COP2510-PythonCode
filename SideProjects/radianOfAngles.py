import math


def convertAngle(num):
    convertedValue = math.radians(num)
    return convertedValue


def main():
    angle = int(input("What is the angle you want to convert to radians?: "))
    result = convertAngle(angle)
    print(result)


main()
