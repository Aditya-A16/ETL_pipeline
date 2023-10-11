import sqlite3
from transform import df2
from extractor import df
import logging
logging.basicConfig(level= logging.INFO, filename= "logs.log", filemode="w", 
                    format="%(asctime)s - %(levelname)s - %(message)s ")
logger = logging.getLogger(__name__)
logger.info("inside load")

def load():
    try:
        #connector to connect to db
        conn = sqlite3.connect("sales.db")

        # Insert the data into the SQLite table
        df.to_sql('Orders', conn, if_exists='replace', index=False)
        df2.to_sql('Product_by_sales', conn, if_exists='replace', index=False)
    except Exception as e:
        logger.exception(e)

        try:
            #execute first query
            cursor = conn.execute('''
            SELECT Product,       
                SUM(month_10 + month_11 + month_12) AS total_sales_last_3_months
            FROM Product_by_sales
            GROUP BY Product
                                    ''')
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(Product_by_sales)")

            # Fetch the results and print column names
            column_names = [row[1] for row in cursor.fetchall()]
            print(column_names)


            #second query
            cursor = conn.execute('''SELECT
                                        product,
                                        COALESCE(SUM(month_1), 0) +
                                        COALESCE(SUM(month_2), 0) +
                                        COALESCE(SUM(month_3), 0) +
                                        COALESCE(SUM(month_4), 0) +
                                        COALESCE(SUM(month_5), 0) +
                                        COALESCE(SUM(month_6), 0) +
                                        COALESCE(SUM(month_7), 0) +
                                        COALESCE(SUM(month_8), 0) +
                                        COALESCE(SUM(month_9), 0) +
                                        COALESCE(SUM(month_10), 0) +
                                        COALESCE(SUM(month_11), 0) +
                                        COALESCE(SUM(month_12), 0) AS total_sales_amount
                                    FROM
                                        Product_by_sales
                                    GROUP BY
                                        product
                                    ORDER BY
                                        total_sales_amount DESC
                                    LIMIT 5;
                                    ''')
            # Fetch the results and print column names
            column_names = [row[1] for row in cursor.fetchall()]
            print(column_names)


            #third query
            cursor = conn.execute('''
                                    SELECT Product,
                                    AVG(month_1 + month_2 + month_3 + month_4 + month_5 + month_6 + month_7 + month_8 + month_9 + month_10 + month_11 + month_12) AS monthly_avg_sales
                                    FROM Product_by_sales
                                    GROUP BY Product	
                                ''')
            # Fetch the results and print column names
            column_names = [row[1] for row in cursor.fetchall()]
            print(column_names)
            cursor.close()
            conn.close()
            
        except Exception as e:
            logger.exception(e)