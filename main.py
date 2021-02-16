# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:34:47 2020

@author: jmorl96
"""

# =============================================================================
# Libraries
# =============================================================================

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os
import inspect
import time
import tqdm


# =============================================================================
# Working Path
# =============================================================================

module_path = inspect.getfile(inspect.currentframe())
module_dir = os.path.realpath(os.path.dirname(module_path))


# =============================================================================
# Input arguments
# =============================================================================
print("Welcome, use this app to transform the new data from INE Data Population Register (>= 2013) to the old format (< 2013)  \n")
print("Write the YEAR of the data:")
year = str(input())

while True:
    try:
            time.strptime(year, '%Y')
            print("Formato Correcto")
            break 
    except:
        print("Wrong format, the correct format is: \n Ex: '2015' ")
        anyo = str(input())

print("Select the file you want to process")
time.sleep(3)

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

# =============================================================================
# Functions
# =============================================================================

def TransfRow(row,year):
#    Linea = Linea.decode("1252")
    row = row[0:17]
    row = row[0:14] + str(int(year) -1 - int(row[15:17]))
#    Linea = Linea.encode("1252")
    return row

# =============================================================================
# Create the new file and process the old file 
# =============================================================================

with open(filename, 'r') as f , open(module_dir +'\PADRON.A' + anyo, 'w') as output:
    
    
    for line in tqdm(f,desc="Processing..." , position=0, leave=True):
        line = TransfRow(line,year)
        output.write(line + '\n')
    f.close()
    output.close()
    print("\n The process has ended,press any key to close the app")
    input()
