# config.py
# Imports, DB connection, colors, SQL extension

import csv
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.cm as cm
import squarify

# Database connection
con = sqlite3.connect("MEA.db")
cur = con.cursor()

# SQL magic for Jupyter
try:
    get_ipython().run_line_magic('load_ext', 'sql')
    get_ipython().run_line_magic('sql', 'sqlite:///MEA.db')
except:
    pass  # Not in Jupyter, skip magic

# Colors for plots
colors = [
    "#becd6f", "#f1b31b", "#ecb792", "#ffb6ca", "#e98103", "#9b2c1b", 
    "#a7b4bb", "#049280", "#8b830d", "#4c5421", "#e05330", "#ef9451", 
    "#4f402e", "#04555a", "#386866", "#6e87a3"
]
