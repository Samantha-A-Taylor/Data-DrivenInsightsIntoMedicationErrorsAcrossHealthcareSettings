missing_data = (incident_data_df.isna() | (incident_data_df == ' ')).sum()
missing_data[missing_data > 0]
