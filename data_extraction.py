import yaml, psycopg2, pandas as pd
from database_utils import DatabaseConnector
from sqlalchemy import create_engine, text, inspect

class DataExtractor:
    engine = DatabaseConnector.db_engine()
    def list_db_tables(engine):
        inspector = inspect(engine)
        inspector.get_table_names()
        with engine.execution_options(isolation_level='AUTOCOMMIT').connect() as connection:
            result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
            for row in result:
                print(row)
    list_table = list_db_tables(engine)

    def read_user_data(engine):
        with engine.execution_options(isolation_level='AUTOCOMMIT').connect() as connection:
            result = pd.read_sql_table('orders_table', engine)
            #result = pd.DataFrame("orders_table")
            isit = result.head(10)
            print(isit)
            return isit
    rud = read_user_data(engine)