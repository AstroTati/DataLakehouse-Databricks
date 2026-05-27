'''____________________________________________________________________________
Data Transformations
Author: Tatiana Rodriguez
Last update: 25/05/2026

This script runs a set of notebooks that apply the necessary transformations 
to the raw data in the bronze layer and creates the silver layer delta tables. 
The notebooks are located in the same folder as this scrip.

It is said that one should work smarter and not harder, hence I am recycling 
the queries from my SQL Data Warehouse project with the necessary syntax 
adjustments. This is why comments throughout these notebooks.
_______________________________________________________________________________
'''

from datetime import datetime

notebooks = [
    "./crm_cust_info_transformandload",
    "./crm_prd_info_transformandload",
    "./crm_sales_details_transformandload",
    "./erp_cust_az12_transformandload",
    "./erp_loc_a101_transformandload",
    "./erp_px_cat_g1v2_transformandload"
]

print(f">>> [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: BEGIN DATA TRANSFORMATION AND LOAD INTO SILVER LAYER")

for nb in notebooks:
    print(f"Running {nb}")
    dbutils.notebook.run(nb, timeout_seconds=0)

print(f">>> [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: DATA TRANSFORMATION AND LOAD INTO SILVER LAYER COMPLETED!")
