import Rachael as R
from Rachael import *

import tkinter as tk
from tkinter import filedialog

#use filedialog from tkinter to alow user to select desired folder using a widget
root = tk.Tk()
root.withdraw()

#get path from selected folder
path = filedialog.askdirectory()

#function to organize the recipes in the selected folder
R.organizeRecipeFiles(path)

#function to choose a random recipe
R.chooseRandomRecipe(path)