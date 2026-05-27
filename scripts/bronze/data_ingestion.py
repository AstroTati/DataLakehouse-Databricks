'''
______________________________________________________________________________
Data Ingestion
Author:         Tatiana Rodriguez
Last update:    25/05/2026

This script creates and bulk load the delta tables required for the project.
We are using the overwrite mode, so be sure to have backups and procede 
with caution.
______________________________________________________________________________
'''

import pyspark.sql
from datetime import datetime

DATA_INGESTION_CONFIG = [
    {
        "source": "crm",
        "path": "/Volumes/catalogue_project1/bronze/raw/source_crm/cust_info.csv",
        "table": "crm_cust_info"
    },
    {
        "source": "crm",
        "path": "/Volumes/catalogue_project1/bronze/raw/source_crm/prd_info.csv",
        "table": "crm_prd_info"
    },
    {
        "source": "crm",
        "path": "/Volumes/catalogue_project1/bronze/raw/source_crm/sales_details.csv",
        "table": "crm_sales_details"
    },
    {
        "source": "erp",
        "path": "/Volumes/catalogue_project1/bronze/raw/source_erp/CUST_AZ12.csv",
        "table": "erp_cust_az12"
    },
    {
        "source": "erp",
        "path": "/Volumes/catalogue_project1/bronze/raw/source_erp/LOC_A101.csv",
        "table": "erp_loc_a101"
    },
    {
        "source": "erp",
        "path": "/Volumes/catalogue_project1/bronze/raw/source_erp/PX_CAT_G1V2.csv",
        "table": "erp_px_cat_g1v2"
    }]

#---------------------------------------------------------------------------------

print(f">>> [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: BEGIN DATA INGESTION")

for item in DATA_INGESTION_CONFIG:
    print(f"Ingesting {item['source']} data into catalogue_project1.{item['table']}")

    df = (
        spark.read
             .option("header", "true")
             .option("inferSchema", "true")
             .csv(item["path"])
    )
    
    df = (
        df.write
          .mode("overwrite")
          .format("delta")
          .saveAsTable(f"catalogue_project1.bronze.{item['table']}")
    )

print(f">>> [{datetime.now()}]: DATA INGESTION COMPLETED!")
