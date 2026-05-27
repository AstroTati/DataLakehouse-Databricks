'''____________________________________________________________________________
Gold layer creation
Author: Tatiana Rodriguez
Last update: 27/05/2026

This script runs a set of notebooks that create the gold layer delta tables. 
The notebooks are located in the same folder as this script and are written in 
SQL for simplicity. Business rules are applied here. The star schema is 
utilized: dimensions and facts. 

It is said that one should work smarter and not harder, hence I am recycling 
the queries from my SQL Data Warehouse project with the necessary syntax 
adjustments. This is why comments throughout these notebooks.
_______________________________________________________________________________
'''

from datetime import datetime

notebooks = [
    "./dim_customers_create",
    "./dim_products_create",
    "./fact_sales_create"
]

print(f">>> [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: BEGIN CREATION OF GOLD LAYER")

for nb in notebooks:
    print(f"Running {nb}")
    dbutils.notebook.run(nb, timeout_seconds=0)

print(f">>> [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: CREATION OF GOLD LAYER COMPLETED!")
