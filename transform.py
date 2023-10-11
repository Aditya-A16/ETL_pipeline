from extractor import df
import pandas as pd
import logging
logging.basicConfig(level= logging.INFO, filename= "logs.log", filemode="w",
                     format="%(asctime)s - %(levelname)s - %(message)s ")
logger = logging.getLogger(__name__)
logger.info("inside transform")

def transform():
    try:
        #calc total sales
        df["total_sales"] = df['Quantity Ordered'] * df['Price Each']

        # calc order month 
        df['Order_Month'] = df['Order Date'].dt.month

        #fill 0 in months where no sale was made
        all_months = pd.DataFrame({'Order_Month': range(1, 13)})
        df = pd.merge(all_months, df, on='Order_Month', how='left')
        df.fillna(0, inplace=True)

        #prepare data set for sql insertion
        df['Order_Month'] = df['Order_Month'].apply(lambda x: 'month_' + str(x))
        df = df.groupby(['Product', 'Order_Month'])['total_sales'].sum().reset_index()
        df2 = df.pivot_table(index=['Product'], columns='Order_Month', values='total_sales', fill_value=0).reset_index()
        df2 = df2.iloc[1:,:].reset_index(drop=True)

    except Exception as e:
        logger.exception(e)