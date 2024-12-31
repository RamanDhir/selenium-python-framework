import csv

def getCSVData(fileName):
    # create an empty list to store rows
    rows = []

    # open the CSV file
    dataFile = open(fileName,"r")

    # create a CSV reader from CSV file, which will read the data line by line
    reader = csv.reader(dataFile)

    # skip the headers of the CSV file
    next(reader)

    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows