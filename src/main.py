# main.py
# Script to run full analysis

from data_processing import load_csv, clean_data, save_to_db
from plots.plot_med_errors import plot_top_med_errors
from plots.plot_guideline_errors import plot_guideline_distribution

def main():
    df = load_csv()
    df_clean = clean_data(df)
    save_to_db(df_clean)
    
    # Example plots
    plot_top_med_errors()
    plot_guideline_distribution()

if __name__ == "__main__":
    main()
