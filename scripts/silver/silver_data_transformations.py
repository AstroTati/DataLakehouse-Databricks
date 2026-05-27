'''____________________________________________________________________________
Data Transformations
Author: Tatiana Rodriguez
Last update: 25/05/2026

This script runs a set of notebooks that apply the necessary transformations 
to the raw data in the bronze layer and creates the silver layer delta tables. 
_______________________________________________________________________________
'''

from datetime import datetime

notebooks = [
    "./crm_cust_info_transformandload.ipynb",
    "./crm_prd_info_transformandload.ipynb",
    "./crm_sales_details_transformandload.ipynb",
    "./erp_cust_az12_transformandload.ipynb",
    "./erp_loc_a101_transformandload.ipynb",
    "./erp_px_cat_g1v2_transformandload.ipynb"
]

print(f">>> [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: BEGIN DATA TRANSFORMATION AND LOAD INTO SILVER LAYER")

for nb in notebooks:
    print(f"Running {nb}")
    dbutils.notebook.run(nb, timeout_seconds=0)

print(f">>> [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: DATA TRANSFORMATION AND LOAD INTO SILVER LAYER COMPLETED!")
