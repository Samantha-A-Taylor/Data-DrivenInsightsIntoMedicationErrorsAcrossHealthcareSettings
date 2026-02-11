# plot_workflow_errors.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from config import con, colors

def plot_process_errors():
    process_errors = pd.read_sql("""
    SELECT 
        MedProcess,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY MedProcess
    ORDER BY IncidentCount DESC;
    """, con)

    process_errors_sorted = process_errors.sort_values('IncidentCount')
    plt.figure(figsize=(12, 6))
    plt.barh(process_errors_sorted['MedProcess'].str[:40], process_errors_sorted['IncidentCount'], color=colors[-7:])
    plt.xlabel("Incident Count", fontsize=12, fontweight='bold')
    plt.ylabel("Medication Process Step", fontsize=12, fontweight='bold')
    plt.title("Distribution of Medication Errors Across Medication Use Process Steps", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


def plot_workflow_boxplots():
    df_workflow_detailed = pd.read_sql("""
    SELECT 
        MedProcess,
        MedErrorCategory,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY MedProcess, MedErrorCategory
    HAVING COUNT(*) >= 20
    ORDER BY IncidentCount DESC;
    """, con)

    plt.figure(figsize=(12,6))
    sns.boxplot(x='IncidentCount', y='MedProcess', data=df_workflow_detailed, orient='h', palette=colors)
    plt.xlabel("Incident Count", fontsize=12)
    plt.ylabel("Workflow Stage (MedProcess)", fontsize=12)
    plt.title("Variation of Medication Errors Across Workflow Stages by Error Type", fontsize=14, fontweight='bold')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
