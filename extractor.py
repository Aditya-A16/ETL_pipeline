import pandas as pd
import os
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level= logging.INFO, filename= "logs.log", filemode="w",
                     format="%(asctime)s - %(levelname)s - %(message)s ")
logger = logging.getLogger(__name__)
logger.info("inside extractor")

def extract():
    try:
        # Directory where your CSV file is located
        directory = "C:\\Users\\adity\\OneDrive\\Desktop\\IT"

        # List all files in the directory
        files = os.listdir(directory)

        # Iterate through the files and find those with a .csv extension
        csv_files = [file for file in files if file.endswith(".csv")]

        # Pick the first match
        filename = csv_files[0]

        #extract and drop empty columns
        df = pd.read_csv(filename)
        df = df.dropna()

        #remove incorrect data
        df = df[df['Order ID'] != 'Order ID']

        #set appropriate dtype for columns
        data_types = {'Order ID': int, 'Product': str, 'Quantity Ordered': int, 'Price Each': float,  'Order Date': 'datetime64', 'Purchase Address':str}
        df = df.astype(data_types)



        #plot box-whisker to detect anomalous data
        plt.boxplot(df["Price Each"])
        plt.boxplot(df["Quantity Ordered"])
    
    except Exception as e:
        logger.exception(e)