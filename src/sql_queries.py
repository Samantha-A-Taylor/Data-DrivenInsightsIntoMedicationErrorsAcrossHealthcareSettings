# sql_queries.py
# All SQL queries as strings for %sql or pd.read_sql

incident_count_by_harm = """
%%sql
SELECT 
    ReportedDegreeofHarm,
    COUNT(*) AS Occurrence_Count
FROM IncidentData
GROUP BY ReportedDegreeofHarm
ORDER BY Occurrence_Count DESC;
"""

top_med_error_categories = """
%%sql
SELECT 
    MedErrorCategory,
    COUNT(*) AS Occurrence_Count
FROM IncidentData
GROUP BY MedErrorCategory
ORDER BY Occurrence_Count DESC
LIMIT 5;
"""

med_error_by_harm = """
%%sql
SELECT 
    MedErrorCategory,
    ReportedDegreeofHarm,
    COUNT(*) AS Occurrence_Count
FROM IncidentData
GROUP BY MedErrorCategory, ReportedDegreeofHarm
HAVING Occurrence_Count >= 20 AND ReportedDegreeofHarm != "No Harm"
ORDER BY Occurrence_Count DESC
LIMIT 10;
"""

# Add all other SQL queries similarly...
