# ETL Pipeline

## Project Description
The ETL (Extract, Transform, Load) Pipeline is a Python project designed to automate the process of extracting sales data from a CSV file, performing data preprocessing and transformation, and then loading the transformed data into a SQLite3 database. The project also includes three predefined SQL queries to retrieve specific information from the database.

The ETL process can be broken down into the following steps:

Extract: Sales data is extracted from the provided CSV file (sales.csv).
Transform: Data preprocessing and transformation take place in this step, where new columns are created as required.
Load: The transformed data is loaded into a SQLite3 database, and three predefined SQL queries can be executed on this database to retrieve meaningful insights.

## Directory Tree
ETL Pipeline\
|\
├── root (Root Directory)\
|   ├── main.py\
|   ├── extractor.py\
|   ├── transform.py\
|   ├── load.py\
|   ├── sales.csv\
|   ├── ETL_notebook.ipynb\
|   └── requirements.txt

# Instructions to Run the Code
o run the ETL pipeline and process the sales data, follow these steps:

1. Ensure the CSV File: Make sure that the sales.csv file is located in the root directory. This file should contain the sales data you want to process.

2. Create a Virtual Environment (Optional but recommended): It's a good practice to create a virtual environment to isolate the project dependencies. You can create a virtual environment using the following command:

    ```
    python -m venv venv

    ```
    Activate the virtual environment before proceeding:
    * On Windows:
        
        ```
        venv\Scripts\activate

        ``` 
    * On macOS and Linux:

        ```
        source venv/bin/activate

        ```
3. Install Project Dependencies: Install the required Python packages by running the following command. This command will install the dependencies listed in requirements.txt.

```
pip install -r requirements.txt
```
4. Run the ETL Pipeline: Execute the main script main.py to start the ETL process. This script will perform data extraction, transformation, and loading into the SQLite3 database.

```
python main.py
```
5. Explore the Data (Optional): You can use the ETL_notebook.ipynb Jupyter notebook to explore the data and test the ETL process step by step.

6. Execute SQL Queries: Once the data is loaded into the SQLite3 database, you can execute predefined SQL queries to retrieve specific information. These queries should be available in your Python scripts (e.g., main.py, load.py).

That's it! You've successfully run the ETL pipeline to extract, transform, and load the sales data into a SQLite3 database and can now explore and analyze the data as needed