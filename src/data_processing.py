# data_processing.py
# Load, clean, and save data to SQLite

import pandas as pd
from config import con

def load_csv(file_path='nrls_data_open.csv'):
    return pd.read_csv(file_path)

def clean_data(df):
    df_clean = df.copy()
    
    # Columns where blanks should become 'Unknown'
    blank_cols = [
        'incidentID', 'Guidelinesinvolved2', 'Guidelinesinvolved3', 'DoublecheckGuidelinecausecategory',
        'ApprovedNameDrug1', 'ApprovedNameDrug2', 'ProprietaryNameDrug1', 'ProprietaryNameDrug2',
        'RouteDrug1', 'SpecialtyLvl1', 'SpecialtyLvl2', 'Locationlvl2'
    ]
    df_clean[blank_cols] = df_clean[blank_cols].replace(' ', 'Unknown')

    # Columns where NULL/NaN should become 'Unknown'
    null_cols = [
        'Guidelineinvolved1', 'ApprovedNameDrug1', 
        'ApprovedNameDrug2', 'ProprietaryNameDrug1'
    ]
    df_clean[null_cols] = df_clean[null_cols].fillna('Unknown')
    
    return df_clean

def save_to_db(df, table_name="IncidentData"):
    df.to_sql(table_name, con, if_exists="replace", index=False)
