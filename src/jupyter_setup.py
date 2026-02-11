!pip install pandas
!pip install squarify
import csv, sqlite3, pandas as pd, matplotlib.pyplot as plt, seaborn as sns, matplotlib.cm as cm, squarify

con = sqlite3.connect("MEA.db")
cur = con.cursor()

%load_ext sql
%sql sqlite:///MEA.db
