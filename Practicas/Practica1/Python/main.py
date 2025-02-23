import serial
from Unidad1.TrabajoClase import InitialPopulation as VGR

if __name__ == "__main__":
    arduino = serial.Serial('com3', baudrate=9600, timeout=1)
    export = [["value1", "value2", "value3", "value4", "vO"]]
    while len(export) < 101:
        try:
            reading = arduino.readline().decode().strip().split("-")
            if len(reading) == 6:
                reading.pop(0)
                reading.pop(-1)
                for i in range(len(reading)):
                    reading[i] = int(reading[i])
                reading.append(VGR.CalculateVO(reading))
                for i in range(len(reading)):
                    reading[i] = str(reading[i])
                export.append(reading)
        except:
            print("Bad Reading")

    with open(file="export.csv", mode="w", encoding="utf-8") as exportFile:
        for reading in export:
            exportFile.write(",".join(reading) + "\n")
