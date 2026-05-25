'''
____________________________________________________________________________________________
Initialization script
Author: Tatiana Rodriguez
Latest update: 25.05.2026


This script selects which catalogue to use, creates the schemas if they don't already exist,
and creates the volume(s) if it doesn't already exist. 
Nothing is dropped nor overwritten.
_____________________________________________________________________________________________
'''

import pyspark.sql

# Define directories, files, and comments
catalogues = ["catalogue_project1"]

schemas = {
    "bronze": "Creating Bronze schema (raw data)...",
    "silver": "Creating Silver schema (cleaned, standardized, and normalized data)...",
    "gold": "Creating Gold schema (business-ready data)..."
}

volumes = {
    "raw": "Volume for raw source files (CSV files).",
}

# -------------------------------------------------------------------

for catalogue_name in catalogues:

    spark.sql(f"USE CATALOG {catalogue_name}")

    for schema_name, comment in schemas.items():
        spark.sql(f"""
            CREATE SCHEMA IF NOT EXISTS {schema_name}
            COMMENT '{comment}'
        """)

    for volume_name, comment in volumes.items():
        spark.sql(f"""
            CREATE VOLUME IF NOT EXISTS bronze.{volume_name}
            COMMENT '{comment}'
        """)
