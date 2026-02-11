# Analysis

This repository contains a modular Python project for analyzing medication error incidents from NRLS data. It includes data cleaning, SQL queries, and visualization scripts.

## Folder Structure

src/  
│  
├── config.py              # Database connection, colors, imports  
├── data_processing.py     # CSV loading, cleaning, saving to DB  
├── sql_queries.py         # SQL queries stored as raw strings  
├── plots/                 # All plotting scripts  
│   ├── plot_med_errors.py  
│   ├── plot_guideline_errors.py  
│   ├── plot_workflow_errors.py  
│   ├── plot_yearly_trends.py  
│   └── plot_locations.py  
└── main.py                # Run full analysis sequentially  

## Installation

1. Clone the repository:  
git clone <repo-url>  
cd <repo-folder>  

2. Create a virtual environment (recommended):  
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate     # Windows  

3. Install dependencies:  
pip install -r requirements.txt  

## Usage

### Jupyter Notebook
- The code supports Jupyter magics (%sql) for running SQL queries directly in notebooks.  
- Example:  
%load_ext sql  
%sql sqlite:///MEA.db  

### Running the full analysis script
python src/main.py  

This will:  
1. Load and clean CSV data (nrls_data_open.csv)  
2. Save cleaned data to SQLite (MEA.db)  
3. Generate all plots sequentially  

### Plot Functions
Each plotting module in src/plots/ contains functions that can be called independently, e.g.:  
from plots.plot_med_errors import plot_top_med_errors  
plot_top_med_errors()  

## Notes
- All %sql magic queries are preserved as-is from the original notebook.  
- Database and plot colors are centralized in src/config.py
