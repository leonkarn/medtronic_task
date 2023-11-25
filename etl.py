import pandas as pd
from sqlalchemy import create_engine
import os

def run_etl():
    # Production Database Configuration
    db_config = {
        "dbname": os.environ.get("PROD_DB_NAME"),
        "user": os.environ.get("PROD_DB_USER"),
        "password": os.environ.get("PROD_DB_PASSWORD"),
        "host": os.environ.get("PROD_DB_HOST")
    }

    # Analytics Database Configuration
    analytics_db_config = {
        "dbname": os.environ.get("ANALYTICS_DB_NAME"),
        "user": os.environ.get("ANALYTICS_DB_USER"),
        "password": os.environ.get("ANALYTICS_DB_PASSWORD"),
        "host": os.environ.get("ANALYTICS_DB_HOST")
    }

    # Create connection engines
    engine = create_engine(f'postgresql+psycopg2://{db_config["user"]}:'
                           f'{db_config["password"]}@{db_config["host"]}/{db_config["dbname"]}')

    analytics_engine = create_engine(f'postgresql+psycopg2://{analytics_db_config["user"]}:'
                                     f'{analytics_db_config["password"]}@{analytics_db_config["host"]}/{analytics_db_config["dbname"]}')

    sql_query = """
        SELECT hobby_name,join_year
        FROM hobbies
        JOIN user_hobbies ON user_hobbies.hobby_id = hobbies.hobby_id
        JOIN users ON user_hobbies.user_id = users.user_id
    """

    # Execute the query and load into a DataFrame
    df = pd.read_sql(sql_query, engine)
    df["id"] = df.index

    with analytics_engine.connect() as connection:
        connection.execute("TRUNCATE TABLE hobbies_analysis;")

    # Load DataFrame to Analytics Database
    df.to_sql('hobbies_analysis', con=analytics_engine, if_exists='append', index=False)

    # Display the DataFrame
    print(df)
    print("Data was ingested succesfully into analytics db")

run_etl()