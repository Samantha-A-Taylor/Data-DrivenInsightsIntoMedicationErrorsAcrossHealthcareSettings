
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


def plot_guideline_lollipop():
    df_guideline_nested = pd.read_sql("""
    SELECT 
        Guidelinecausecategory,
        MedErrorCategory,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY Guidelinecausecategory, MedErrorCategory
    ORDER BY IncidentCount DESC;
    """, con)

    df_guideline_agg = df_guideline_nested.groupby('Guidelinecausecategory')['IncidentCount'].sum().reset_index()
    df_guideline_agg = df_guideline_agg.sort_values('IncidentCount')

    plt.figure(figsize=(10, 6))
    plt.hlines(y=df_guideline_agg['Guidelinecausecategory'], xmin=0, xmax=df_guideline_agg['IncidentCount'], color='#f1b31b', linewidth=3)
    plt.plot(df_guideline_agg['IncidentCount'], df_guideline_agg['Guidelinecausecategory'], "o", color='#eb8002', markersize=8)
    plt.xlabel("Incident Count", fontsize=12, fontweight='bold')
    plt.ylabel("Guideline Cause Category", fontsize=12, fontweight='bold')
    plt.title("Medication Errors by Guideline Cause Category with Error Type Context", fontsize=14, fontweight='bold')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
