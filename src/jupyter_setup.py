!pip install pandas
!pip install squarify
import csv, sqlite3, pandas as pd, matplotlib.pyplot as plt, seaborn as sns, matplotlib.cm as cm, squarify

con = sqlite3.connect("MEA.db")
cur = con.cursor()

%load_ext sql
%sql sqlite:///MEA.db

  colors = ["#becd6f", "#f1b31b", "#ecb792", "#ffb6ca", "#e98103", "#9b2c1b", 
          "#a7b4bb", "#049280", "#8b830d", "#4c5421", "#e05330", "#ef9451", 
          "#4f402e", "#04555a", "#386866", "#6e87a3"]
