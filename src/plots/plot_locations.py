# plot_locations.py
import matplotlib.pyplot as plt
import pandas as pd
from config import con, colors

def plot_care_and_locations():
    df_care = pd.read_sql("""
    SELECT 
        CareSettingofOccurrence,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY CareSettingofOccurrence
    ORDER BY IncidentCount DESC
    LIMIT 5;
    """, con)

    df_loc1 = pd.read_sql("""
    SELECT 
        Locationlvl1,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY Locationlvl1
    ORDER BY IncidentCount DESC
    LIMIT 5;
    """, con)

    df_loc2 = pd.read_sql("""
    SELECT 
        Locationlvl2,
        COUNT(*) AS IncidentCount
    FROM IncidentData
    GROUP BY Locationlvl2
    ORDER BY IncidentCount DESC
    LIMIT 8;
    """, con)

    fig, axes = plt.subplots(3, 1, figsize=(12, 24))

    # Care Setting pie
    patches, _, _ = axes[0].pie(df_care['IncidentCount'], labels=None, autopct='%1.1f%%', startangle=90, pctdistance=1.1, colors=colors)
    axes[0].legend(patches, df_care['CareSettingofOccurrence'].str[:38], title="Care Setting", fontsize=12, title_fontsize=12, bbox_to_anchor=(1, 1))
    axes[0].set_title("Medication Errors by Care Setting", fontsize=14, fontweight='bold')

    # Locationlvl1 pie
    patches, _, _ = axes[1].pie(df_loc1['IncidentCount'], labels=None, autopct='%1.1f%%', startangle=90, pctdistance=1.1, colors=colors[4:])
    axes[1].legend(patches, df_loc1['Locationlvl1'], title="Location lvl1", fontsize=12, title_fontsize=12, bbox_to_anchor=(1, 1))
    axes[1].set_title("Medication Errors by Primary Location (Locationlvl1)", fontsize=14, fontweight='bold')

    # Locationlvl2 pie
    patches, _, _ = axes[2].pie(df_loc2['IncidentCount'], labels=None, autopct='%1.1f%%', startangle=90, pctdistance=1.1, colors=colors[8:])
    axes[2].legend(patches, df_loc2['Locationlvl2'], title="Location lvl2", fontsize=12, title_fontsize=12, bbox_to_anchor=(1, 1))
    axes[2].set_title("Medication Errors by Detailed Location (Locationlvl2)", fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.show()
