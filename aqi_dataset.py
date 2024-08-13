import psycopg2
import pandas as pd

# Database connection details
conn = psycopg2.connect(
        dbname='medpiperdatabase',
        user='postgres',
        password='POSTSQLkashi@0025',
        host='localhost',
        port='5432'
    )
    
cursor = conn.cursor()

cursor.execute( '''
CREATE TABLE IF NOT EXISTS airquality (
    id SERIAL PRIMARY KEY,
    AQI TEXT,
    Category VARCHAR(255),
    Diseases TEXT,
    Health_Checkup TEXT
)
''')


df = pd.read_csv('AQI_Dataset.csv')


# Insert the data into the table
for row in df.itertuples(index=False):
    cursor.execute(
        '''
        INSERT INTO airquality (AQI, Category, Diseases, Health_Checkup)
        VALUES (%s, %s, %s, %s)
        ''',
        row
    )

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

