#hw5
#Will Frazier and Alex Berry

import csv
import numpy as np

def read_file(filename):
    x = []
    country = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, quotechar='|')
        next(reader)
        for row in reader:
            country.append(row[0])
            entry = [float(i) for i in row[1:]]
            x.append(np.array(entry))
    return x
    
