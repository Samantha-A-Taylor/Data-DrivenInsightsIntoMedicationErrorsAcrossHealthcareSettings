# plot_guideline_errors.py
import matplotlib.pyplot as plt
import squarify
import pandas as pd
from config import con, colors

def plot_guideline_distribution():
    df_guideline = pd.read_sql("""
    SELECT 
        Guidelinecausecategory,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY Guidelinecausecategory
    ORDER BY IncidentCount DESC
    LIMIT 15;
    """, con)

    plt.figure(figsize=(12, 8))
    squarify.plot(
        sizes=df_guideline['IncidentCount'],
        label=df_guideline['Guidelinecausecategory'],
        alpha=0.8,
        color=colors[:len(df_guideline)]
    )
    plt.title("Distribution of Medication Errors by Guideline Cause Category", fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.show()

# Other lollipop/detailed guideline plots can go here
