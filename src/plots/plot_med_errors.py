# plot_med_errors.py
# Plots for medication errors

import matplotlib.pyplot as plt
import pandas as pd
from config import con, colors

def plot_top_med_errors():
    mec_errors = pd.read_sql("""
    SELECT 
        MedErrorCategory,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY MedErrorCategory
    ORDER BY IncidentCount DESC
    LIMIT 10;
    """, con)

    plt.figure(figsize=(8, 8))
    patches, _, autotexts = plt.pie(
        mec_errors['IncidentCount'],
        labels=None,
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=1.1,
        colors=colors
    )
    plt.legend(patches, mec_errors['MedErrorCategory'].str[:40], title="MedErrorCategory", bbox_to_anchor=(1, 1))
    plt.title("Distribution of Medication Errors Across 10 Most Frequent Categories", fontsize=14, fontweight='bold')
    plt.show()

# Add other plots for drug1, drug2 similarly...
