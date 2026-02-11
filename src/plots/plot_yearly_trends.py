# plot_yearly_trends.py
import matplotlib.pyplot as plt
import pandas as pd
from config import con, colors

def plot_yearly_incidents():
    df_year = pd.read_sql("""
    SELECT 
        Year_of_Occurrence,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY Year_of_Occurrence
    ORDER BY Year_of_Occurrence;
    """, con)

    plt.figure(figsize=(12,6))
    plt.plot(df_year['Year_of_Occurrence'], df_year['IncidentCount'], marker='o', color='#f1b31b', linewidth=2)
    plt.xlabel("Year", fontsize=12, fontweight='bold')
    plt.ylabel("Incident Count", fontsize=12, fontweight='bold')
    plt.title("Medication Error Incident Trends by Year", fontsize=14, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


def plot_yearly_harm_trends():
    df_year_harm = pd.read_sql("""
    SELECT 
        Year_of_Occurrence,
        ReportedDegreeofHarm,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY Year_of_Occurrence, ReportedDegreeofHarm
    HAVING Year_of_Occurrence >= 2014
    ORDER BY Year_of_Occurrence;
    """, con)

    df_year_harm_pivot = df_year_harm.pivot(index='Year_of_Occurrence', columns='ReportedDegreeofHarm', values='IncidentCount').fillna(0)
    df_year_harm_pivot.plot(figsize=(12,6), marker='o', linewidth=2, color=colors[:len(df_year_harm_pivot.columns)])
    plt.xlabel("Year", fontsize=12, fontweight='bold')
    plt.ylabel("Incident Count", fontsize=12, fontweight='bold')
    plt.title("Medication Error Trends by Year and Reported Harm Severity (2014 Onwards)", fontsize=14, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(title="Harm Level", bbox_to_anchor=(1,1))
    plt.tight_layout()
    plt.show()


def plot_yearly_error_categories():
    df_year_error = pd.read_sql("""
    SELECT 
        Year_of_Occurrence,
        MedErrorCategory,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY Year_of_Occurrence, MedErrorCategory
    HAVING Year_of_Occurrence >= 2014
    ORDER BY Year_of_Occurrence;
    """, con)

    df_year_error_pivot = df_year_error.pivot(index='Year_of_Occurrence', columns='MedErrorCategory', values='IncidentCount').fillna(0)
    df_year_error_pivot.plot(figsize=(14,8), marker='o', linewidth=2, color=colors[:len(df_year_error_pivot.columns)])
    plt.xlabel("Year", fontsize=12, fontweight='bold')
    plt.ylabel("Incident Count", fontsize=12, fontweight='bold')
    plt.title("Trends in Medication Errors by Category (2014 Onwards)", fontsize=14, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend([str(c)[:30] for c in df_year_error_pivot.columns], title="MedErrorCategory", bbox_to_anchor=(1,1))
    plt.tight_layout()
    plt.show()
