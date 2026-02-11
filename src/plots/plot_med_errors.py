# plot_med_errors.py
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
    patches, _, _ = plt.pie(
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


def plot_top_drugs():
    # ApprovedNameDrug1
    drug1_errors = pd.read_sql("""
    SELECT 
        ApprovedNameDrug1,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY ApprovedNameDrug1
    HAVING ApprovedNameDrug1 != 'No Drug Given'
    ORDER BY IncidentCount DESC
    LIMIT 15;
    """, con)

    plt.figure(figsize=(8, 8))
    patches, _, _ = plt.pie(
        drug1_errors['IncidentCount'],
        labels=None, 
        autopct='%1.1f%%',  
        startangle=90,
        pctdistance=1.1,
        colors=colors
    )
    plt.legend(patches, drug1_errors['ApprovedNameDrug1'], title="ApprovedNameDrug1", bbox_to_anchor=(1, 1))
    plt.title("Distribution of Medication Errors Across 15 Drugs (ApprovedNameDrug1)", fontsize=14, fontweight='bold')
    plt.show()


def plot_drug2_combined_vs_top15():
    drug2_errors_all = pd.read_sql("""
    SELECT
        CASE 
            WHEN ApprovedNameDrug2 = 'Unknown' THEN 'Unknown'
            ELSE 'All Other Medications'
        END AS Drug_Name_Status,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY Drug_Name_Status
    HAVING ApprovedNameDrug2 != 'No Drug Given'
    ORDER BY IncidentCount DESC;
    """, con)

    drug2_errors = pd.read_sql("""
    SELECT 
        ApprovedNameDrug2,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY ApprovedNameDrug2
    HAVING ApprovedNameDrug2 != 'Unknown'
    ORDER BY IncidentCount DESC
    LIMIT 15;
    """, con)

    fig, axes = plt.subplots(2, 1, figsize=(8, 10))

    # Combined/Unknown
    patches, _, _ = axes[0].pie(
        drug2_errors_all['IncidentCount'],
        labels=None,
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=1.1,
        colors=colors[1:]
    )
    axes[0].legend(patches, drug2_errors_all['Drug_Name_Status'], title="Drug Name Status", bbox_to_anchor=(1, 1))
    axes[0].set_title("Medication Error Incidents by Drug Identification Status\n(ApprovedNameDrug2)", fontsize=14, fontweight='bold')

    # Top 15 drugs
    patches, _, _ = axes[1].pie(
        drug2_errors['IncidentCount'],
        labels=None,
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=1.1,
        colors=colors
    )
    axes[1].legend(patches, drug2_errors['ApprovedNameDrug2'], title="ApprovedNameDrug2", bbox_to_anchor=(1, 1))
    axes[1].set_title("Top 15 Most Frequently Identified Drugs (ApprovedNameDrug2)", fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.show()
